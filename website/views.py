from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib import messages
from .forms import StickItUserCreationFrom
# Create your views here.
class RegisterService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html', {'form': StickItUserCreationFrom()})
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StickItUserCreationFrom(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('base')
            else:
                messages.error(request, 'Please correct the error below.')
        return render(request, 'register.html', {'form': form})
    

class LoginService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')