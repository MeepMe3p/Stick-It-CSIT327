from django.urls import path
from .views import *

# app_name = "authentication"
urlpatterns = [
    path('login/', LoginUser.as_view(), name = "login"),

    path('register/', RegisterService.as_view(), name='register'),
]
