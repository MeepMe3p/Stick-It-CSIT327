from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login,authenticate,get_user_model
from .forms import StickItLoginForm
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StickItUserCreationFrom

# Create your views here.
class LoginUser(View):
    def get(self,request):
        print("rungging")
        return render(request,"authentication/login2.html",{'form':StickItLoginForm()})
        
    
    def post(self,request):
        UserModel = get_user_model()
        

        
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            print("this run3")

            messages.success(request,"Successfully logged in")
            return redirect('note:home')
        else:
            messages.error(request,"Incorrect username or password")
            # return render(request,'login.html',{'form':StickItLoginForm()})
            return render(request,'authentication/login2.html',{'form':StickItLoginForm()})


class RegisterService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/register2.html', {'form': StickItUserCreationFrom()})
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StickItUserCreationFrom(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('note:home')
            else:
                messages.error(request, 'Please correct the error below.')
        return render(request, 'authentication/register2.html', {'form': form})