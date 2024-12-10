from django.contrib import admin
from .models import Board, Category, Notification

# Register your models here.
admin.site.register(Board)
admin.site.register(Category)
admin.site.register(Notification)