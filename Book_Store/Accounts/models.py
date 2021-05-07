from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Contact_number = models.CharField(max_length=10, unique=True)
    # first_name = models.CharField(max_length=256, blank=True, null=True)
    