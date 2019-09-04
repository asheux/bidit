"""Imports"""

from django.contrib.auth.models import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    """User manager"""

    def create_user(self, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, password
        and other extra fields living in **kwargs.
        """
        if not email:
            return ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email, password
        and other extra fields living in **kwargs.
        """
        kwargs.setdefault('is_admin', True)

        if kwargs.get('is_superuser') is not True:
            return ValueError('Supueruser must have an is_superuser set to True')
        return self.create_user(email, password, **kwargs)


class ItemManager(models.Manager):
    """
    Item manager
    """
    def create_item(self, owner, **kwargs):
        """ Creates a new item """

        if not owner:
            return ValueError("You must be a user to create an item")

        item = self.model(owner, **kwargs)
        item.save(self._db)

        return item







