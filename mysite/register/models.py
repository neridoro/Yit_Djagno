from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
#extention of base user from djagno models.
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        primary_key=True,
    )
    first_name = models.CharField("first name", max_length=30, blank=True)
    last_name = models.CharField("last name", max_length=30, blank=True)
    REQUIRED_FIELDS = ['first_name','last_name']