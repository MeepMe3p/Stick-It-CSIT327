from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Programmer Name: Elijah Rei Sabay
# I created this category for searching purposes, feel nako lisod if di sha iseparate entity
class Category(models.Model):
    category_name = models.CharField(max_length=30,unique=True)
    category_description = models.TextField(max_length=100)

    def __str__(self):
        return self.category_name;
class Board(models.Model):
    board_name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    # owner = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    PRIVACY_TYPE = [
        ("PV" , "Private"),
        ("PB" , "Public")
    ]
    privacy_settings = models.CharField(choices=PRIVACY_TYPE, max_length=2)
    date_created = models.DateField(auto_now_add=True)

    # according do documentation standard of many to many is plural
    users = models.ManyToManyField(User)
    user_count = models.IntegerField(default=1) 
