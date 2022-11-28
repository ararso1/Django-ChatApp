from django.db import models
from django.contrib.auth.models import User
import time

# Create your models here.

class User_profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200,null=True)
    mid_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    locaton = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
	    return self.first_name

class Post(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=200,null=True)
    image = models.ImageField(null=True, blank=True)
    time = models.TimeField(null=True)
    def __str__(self):
	    return self.text