from django.urls import path
from . import views
# from .views import CreateBoardView, PracticeView

app_name = "board"
urlpatterns = [
    # path('create-board/',CreateBoardView.as_view(),name = "create_table"),
    path('create-board/', views.create_board, name='create_board'),
    path('home/<int:category_id>/', views.filter_boards_by_category, name='filter_boards_by_category'),
    path('my-space/<int:category_id>/', views.filter_boards_by_category, 
         {'template_name': 'mainApp/my_space.html'}, name='filter_boards_by_category_my_space'),
    path('my_board/', views.render_board, name='render_board'),
    path('join-board/<int:board_id>/', views.join_board, name='join_board'),
    path('board/<int:pk>/', views.BoardDetailView.as_view(), name='board_detail')
]
