from django.urls import path
from .views import LoginUser

app_name = "authentication"
urlpatterns = [
    path('login/', LoginUser.as_view(), name = "login"),

]
