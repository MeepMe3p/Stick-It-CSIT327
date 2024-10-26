from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from .forms import StickItLoginForm
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from .forms import StickItUserCreationForm
<<<<<<< Updated upstream

# Create your views here.
class LoginUser(View):
    def get(self,request):
        print("rungging")
        return render(request,"authentication/login2.html",{'form':StickItLoginForm()})
        
    
    def post(self,request):
        UserModel = get_user_model()
        
        print(request.POST)
        user = authenticate(request,username = request.POST['email'], password = request.POST['password'])
        print(user)
        if user is not None:
            login(request,user)
            print("this run3")

            messages.success(request,"Successfully logged in")
            return redirect('mainApp:home')
=======
from django.contrib.auth.forms import UserCreationForm

def registerPage(request):
        if request.user.is_authenticated:
             return redirect('mainApp:home')
>>>>>>> Stashed changes
        else:
            form = StickItUserCreationForm()

            if request.method == 'POST':
                form = StickItUserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('first_name')
                    messages.success(request, 'Account was created for ' + user)

                    return redirect('authentication:login')

            context = {'form': form}
            return render(request, 'authentication/register2.html', context)


<<<<<<< Updated upstream
class RegisterService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authentication/register2.html', {'form': StickItUserCreationForm()})
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StickItUserCreationForm(request.POST)
            if form.is_valid():
                print("Form is valid")
                user = form.save()
                login(request, user)
                messages.success(request, 'Account created successfully!')
                return redirect('authentication:login')
            else:
                messages.error(request, 'Please correct the error below.')
                print(form.errors)
        return render(request, 'authentication/register2.html', {'form': form})
=======
def loginPage(request):
    if request.user.is_authenticated:
         return redirect('mainApp:home')
    
    form = StickItLoginForm(data=request.POST)
    if request.method == 'POST':
        print(request.POST)

        if form.is_valid():
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            print("Form is valid")
            user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
            if user is not None:
                # login(request, form.get_user())
                print("User is not none")
                login(request, user)
                return redirect('mainApp:home')
        else:
            print(form.errors)
            messages.info(request, 'Email or password is incorrect')

    context = {'form':form}
    return render(request, 'authentication/login2.html', context)


def logoutPage(request):
    logout(request)
    return redirect('authentication:login')
>>>>>>> Stashed changes
