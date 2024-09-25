from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = "stickit"
urlpatterns = [
    path('', LoginService.as_view(), name = 'base'),
    path('register/', RegisterService.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = "authentication:login"), name = "logout"),
    path('home/', HomeView.as_view() ,name = "home"),

]