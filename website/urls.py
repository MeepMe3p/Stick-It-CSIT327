from django.urls import path
from . views import *

urlpatterns = [
    path('', LoginService.as_view(), name = 'base'),
    path('register/', RegisterService.as_view(), name='register')
]