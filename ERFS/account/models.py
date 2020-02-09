from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile/images/")
    bio=models.TextField(max_length=100)
    
def __str__(self):
            return self.user.username


