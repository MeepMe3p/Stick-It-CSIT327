from django.urls import path
from .views import CreateBoardView, PracticeView

app_name = "board"
urlpatterns = [
    path('create-board/',CreateBoardView.as_view(),name = "create_table"),
    path('practice/',PracticeView.as_view(), name = 'practice'),
]
