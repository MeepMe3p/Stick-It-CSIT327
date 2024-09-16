from django.urls import path
from . views import *
from django.contrib.auth.views import LogoutView

# app_name = "notes"
urlpatterns = [
    path('', LoginService.as_view(), name = 'base'),
    path('register/', RegisterService.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = "register"), name = "logout"),
    path('login/', LoginUser.as_view(), name = "login"),
    path('home/', HomeView.as_view() ,name = "home")
]