from ast import Global
from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime


# creating a form 

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from .manager import UserManager
import uuid

class User(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6 ,null=True, blank=True)
   
    slug= models.CharField(max_length=50, default=uuid.uuid4, unique=True)
    phone_num= models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    
class Project(models.Model):
    title= models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(blank=True,null=True)