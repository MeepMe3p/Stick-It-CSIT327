from django.urls import path
from . import views
# from .views import CreateBoardView, PracticeView

app_name = "board"
urlpatterns = [
    # path('create-board/',CreateBoardView.as_view(),name = "create_table"),
    path('create-board/', views.create_board, name='create_board'),
    # path('practice/',PracticeView.as_view(), name = 'practice'),

    # ej changes
    # path('home/<int:category_id>/', views.filter_boards_by_category, name='filter_boards_by_category'), 
    path('update/<int:pk>', views.update_board,name='update_board'),
    path('home/my-board/', views.filter_owner, name='filter_by_owner'),
    path('home/<slug:category_slug>/', views.filter_boards_by_category, name='filter_boards_by_category'),
    path('response/invite/<int:pk>', views.respond_invite,name="respond_invite"),
    path('response/join/<int:pk>', views.respond_join_request,name="respond_join"),
    path('join/<int:pk>',views.join_board, name = "join_board"),
    # 

    # path('home/al', views.all_boards, name='all_boards')
    path('my_board/', views.render_board, name='render_board'),
]
