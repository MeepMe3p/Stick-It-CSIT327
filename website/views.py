import json
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate,get_user_model
from django.contrib import messages
from .forms import StickItUserCreationFrom
from django.template.context import RequestContext

from django.http import JsonResponse
# from django.contrib.auth.views import Temp

# Create your views here.
# PROGRAMMER NAME: AVRIL NIGEL CHUA
class RegisterService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register2.html', {'form': StickItUserCreationFrom()})
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StickItUserCreationFrom(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Please correct the error below.')
        return render(request, 'register2.html', {'form': form})
    

class LoginService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

    
# class Cat
    


class HomeView(View):
    # def get()
    print("welcome home")
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
