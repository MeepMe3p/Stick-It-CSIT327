from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import StickItUserCreationFrom, StickItLoginForm
# from django.contrib.auth.views import Temp

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

# PROGRAMMER NAME: ELIJAH REI SABAY
# test2user - secondpassword
class LoginUser(View):
    # redirect_authenticated_user = True

    def get(self,request):
        print("rungging")
        return render(request, 'login.html',{'form':StickItLoginForm()})
    
    def post(self,request):
        if request.method == "POST":
            # username = request.POST['username']
            # password = request.POST['password']
            user = authenticate(request,username = request.POST['username'], password = request.POST['password'])

            if user is not None:
                login(request,user)
                messages.success(request,"Successfully logged in!s")
                return redirect('home')
            else:
                messages.error(request,"Incorrect username or password")
                return render(request,'login.html',{'form':StickItLoginForm()})

class HomeView(View):
    # def get()
    print("welcome home")
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

    