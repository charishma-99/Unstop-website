from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, first_name, last_name, username, gender, phone, organization, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, username=username, gender=gender, phone=phone, organization=organization)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, first_name, last_name, username, gender, phone, organization, password=None):
        """Create a new superuser profile"""
        user=self.create_user(email,first_name, last_name, username, gender, phone, organization, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length = 255, unique = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)

    is_active = models.BooleanField (default=True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username','gender','phone','organization']

    def __str__(self):
        """Return string representation of our user"""
        return f"{self.username}"