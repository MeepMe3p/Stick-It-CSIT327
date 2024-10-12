from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('create-board/', views.create_board, name='create_board'),
] 