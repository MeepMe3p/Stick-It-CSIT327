from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='profile_pics')
    birthdate = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank =True)
    facebook_link = models.TextField(max_length=250, null=True,blank=True)
    facebook_link_hidden = models.BooleanField(null=True, default=True)
    linkedin_link = models.TextField(max_length=250, null=True, blank=True) 
    linkedin_link_hidden = models.BooleanField(null=True, default=True)
    twitter_link = models.TextField(max_length=250, null=True, blank=True)
    twitter_link_hidden = models.BooleanField(null=True, default=True)
    
