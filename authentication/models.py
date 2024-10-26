from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
<<<<<<< Updated upstream
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    # birth_date = models.DateField(null=True, blank=True)
    # phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        username = self.user.first_name + ' ' + self.last_name
        return username
=======
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    # email = models.EmailField(unique=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # password1 = models.CharField(max_length=100)
    # password2 = models.CharField(max_length=100)
    # birth_date = models.DateField(null=True, blank=True)
    # phone_number = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank =True)
    facebook_link = models.TextField(max_length=250, null=True,blank=True)
    facebook_link_hidden = models.BooleanField(null=True, default=True)
    linkedin_link = models.TextField(max_length=250, null=True, blank=True) 
    linkedin_link_hidden = models.BooleanField(null=True, default=True)
    twitter_link = models.TextField(max_length=250, null=True, blank=True)
    twitter_link_hidden = models.BooleanField(null=True, default=True)
    
    def __str__(self):
        return self.user.username

    # @property
    # def username(self):
    #     return f"{self.user.first_name} {self.user.last_name}"
>>>>>>> Stashed changes
