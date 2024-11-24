from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', NoteView.as_view(), name='note'),
    # path('save_note/', NoteCreateView.as_view(), name='save_note'),
    path('update_note/<int:pk>/', NoteUpdateView.as_view(), name='update_note'),
    path('delete_note/<int:pk>/', NoteDeleteView.as_view(), name='delete_note'),
    path('get_notes/', NoteGetView.as_view(), name='get_notes'),
    # Register Views By Avril Nigel Chua - BOGO
    path('base/', LoginService.as_view(), name = 'base'),
    # path('register/', RegisterService.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = "authentication:login"), name = "logout"),
    path('home/', HomeView.as_view() ,name = "home"),
]