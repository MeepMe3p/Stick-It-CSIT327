from django.urls import path
from . import views
from .views import CreateBoardView, PracticeView

app_name = "board"
urlpatterns = [
    path('create-board/',CreateBoardView.as_view(),name = "create_table"),
    path('create-board/', views.create_board, name='create_board'),
    path('practice/',PracticeView.as_view(), name = 'practice'),
]
