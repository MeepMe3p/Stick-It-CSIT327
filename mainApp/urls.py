from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainApp'
urlpatterns = [
     path('home/', views.home, name='home'),
     path('my_space/', views.my_space, name='my_space'),
     path('my_space/edit_profile', views.edit_profile, name='edit_profile'),
     # path('logout/', views.logoutPage , name = "logout"),
     path('board/', include('board.urls', namespace='board')),
]
