from django.urls import path
from .consumers import NoteConsumer

websocket_urlpatterns = [
    path('ws/<str:note_board_name>/', NoteConsumer.as_asgi()),
]