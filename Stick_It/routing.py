from django.urls import path
from note.consumers import NoteConsumer
from board.consumers import NotificationConsumer


websocket_urlpatterns = [
    path('ws/<str:note_board_name>/', NoteConsumer.as_asgi()),
    path('ws/notification/<int:pk>/', NotificationConsumer.as_asgi()),

]