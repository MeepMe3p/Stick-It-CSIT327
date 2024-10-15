from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login,authenticate,get_user_model,logout
from .forms import StickItLoginForm
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StickItUserCreationForm

# Create your views here.
class LoginUser(View):
    def get(self,request):
        print("rungging")
        return render(request,"authentication/login2.html",{'form':StickItLoginForm()})
        
    
    def post(self,request):
        UserModel = get_user_model()
        
        print(request.POST)
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            print("this run3")

            messages.success(request,"Successfully logged in")
            return redirect('mainApp:home')
        else:
            messages.error(request,"Incorrect username or password")
            # return render(request,'login.html',{'form':StickItLoginForm()})
            return render(request,'authentication/login2.html',{'form':StickItLoginForm()})


class RegisterService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/register2.html', {'form': StickItUserCreationForm()})
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StickItUserCreationForm(request.POST)
            if form.is_valid():
                print("Form is valid")
                user =form.save()
            user = authenticate(request,username = request.POST['email'], password = request.POST['password1'])
            print(user)
            if user is not None:
                login(request,user)
                print("this run3")

                # messages.success(request,"Successfully logged in")
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('mainApp:home')
            else:
                messages.error(request, 'Please correct the error below.')
                print(form.errors)
        return render(request, 'authentication/register2.html', {'form': form})
    
def logout_view(request):
    logout(request=request)
    return redirect('authentication:login')