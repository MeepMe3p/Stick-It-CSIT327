from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainApp'
urlpatterns = [
     path('home/', views.home, name='home'),
<<<<<<< Updated upstream
     path('', views.myBoards, name='my_boards'),
     path('', views.profile, name='profile'),
     path('board/', include('board.urls', namespace='board'))
=======
     path('my_space/', views.mySpace, name='my_space'),
     # path('logout/', views.logoutPage , name = "logout"),
     path('board/', include('board.urls', namespace='board')),
>>>>>>> Stashed changes
]
