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
        user = self.model(email=email, first_name=first_name, last_name=last_name,
                          username=username, gender=gender, phone=phone, organization=organization)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, username, gender, phone, organization, password=None):
        """Create a new superuser profile"""
        user = self.create_user(
            email, first_name, last_name, username, gender, phone, organization, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'username', 'gender', 'phone', 'organization']

    def __str__(self):
        """Return string representation of our user"""
        return f"{self.username}"


class Skill(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=250)
    degree = models.CharField(max_length=50)
    from_year = models.CharField(max_length=50)
    to_year = models.CharField(max_length=50)
    percentage = models.IntegerField()
    cgpa = models.FloatField()
    specialization = models.CharField(max_length=250)
    university = models.CharField(max_length=250)
    institution = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user}  {self.qualification}"


class Work_Experience(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    designation = models.CharField(max_length=250)
    sector = models.CharField(max_length=50)
    from_year = models.CharField(max_length=50)
    to_year = models.CharField(max_length=50)
    organization = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=250)
    city = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user}  {self.designation}"


class Profile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    rank = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)
    coins = models.FloatField(default=0)
    country = models.CharField(max_length=250, null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True, max_length=200)
    instagram = models.URLField(null=True, blank=True, max_length=200)
    twitter = models.URLField(null=True, blank=True, max_length=200)
    github = models.URLField(null=True, blank=True, max_length=200)
    work_experience = models.CharField(max_length=50, null=True, blank=True)
    skill = models.ManyToManyField(Skill, null=True, blank=True)
    education = models.ManyToManyField(Education, null=True, blank=True)
    work_history = models.ManyToManyField(Work_Experience, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"
