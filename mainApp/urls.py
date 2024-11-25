from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainApp'
urlpatterns = [
     path('home/', views.home, name='home'),
     # path('my_space/', views.my_space, name='my_space'),
     path('profile/', views.profile, name='profile'),
     path('my_boards/', views.boards, name='my_boards'),
     path('profile/edit_profile', views.edit_profile, name='edit_profile'),
     path('profile/edit_social_links', views.edit_social_links, name='edit_social_links'),
     # path('logout/', views.logoutPage , name = "logout"),
     path('board/', include('board.urls', namespace='board')),
]
