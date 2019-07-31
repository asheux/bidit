from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.db import models
from .managers import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        """Checks if user is a member of the staff"""
        return self.is_superuser

