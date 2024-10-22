from django.urls import path
from . import views
from .views import *

app_name = "board"
urlpatterns = [
    path('create-board/',CreateBoardView.as_view(),name = "create_board"),
    path('update/<int:pk>/', UpdateBoard.as_view(),name='update_board'),
    # path('create-board/', views.create_board, name='create_board'),
    path('practice/',PracticeView.as_view(), name = 'practice'),
]
