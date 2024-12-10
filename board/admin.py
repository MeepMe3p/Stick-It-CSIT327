from django.contrib import admin
from .models import Board, Category, Notification,ProjectBoard,SimpleBoard

# Register your models here.
admin.site.register(Board)
admin.site.register(Category)
admin.site.register(Notification)
admin.site.register(ProjectBoard)
admin.site.register(SimpleBoard)