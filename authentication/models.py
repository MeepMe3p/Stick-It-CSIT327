from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
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