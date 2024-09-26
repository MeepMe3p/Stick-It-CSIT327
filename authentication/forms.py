from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


# PROGRAMMER NAME: ELIJAH REI SABAY
# test2user - secondpassword
class StickItLoginForm(AuthenticationForm):
    print("hello")
    username = forms.EmailField(label = "Email")
    password = forms.CharField(label="Enter Password", widget= forms.PasswordInput(attrs={
        "height":'40px',        
    }))

    class Meta:
        model = User
        fields = ['email','password']
