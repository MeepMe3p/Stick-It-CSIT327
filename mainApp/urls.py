from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainApp'
urlpatterns = [
     # path('home/', views.home, name='home'),
     path('home/', views.Home.as_view(), name='home'),
     path('', views.myBoards, name='my_boards'),
     path('profile/', views.profile, name='profile'),
     # path('board/', include('board.urls', namespace='board'))
]
