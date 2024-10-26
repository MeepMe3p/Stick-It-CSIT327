from django.urls import path
from . import views

app_name = "authentication"
urlpatterns = [
<<<<<<< Updated upstream
    path('login/', LoginUser.as_view(), name = "login"),
    path('register/', RegisterService.as_view(), name='register'),
=======
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutPage , name = "logout"),
>>>>>>> Stashed changes
]