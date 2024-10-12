from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('', views.myBoards, name='my_boards'),
     path('', views.profile, name='profile'),
     path('', include('boards.urls', namespace='boards'))
]
