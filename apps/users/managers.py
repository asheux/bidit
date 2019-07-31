from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

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
            return valueError('Supueruser must have an is_superuser set to True')
        self.create_user(email, password, **kwargs)

        return user

