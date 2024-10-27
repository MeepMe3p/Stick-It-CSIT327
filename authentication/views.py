from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import StickItLoginForm, StickItUserCreationForm

def register_page(request):
        if request.user.is_authenticated:
             return redirect('mainApp:home')
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


def login_page(request):
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


def logout_page(request):
    logout(request)
    return redirect('authentication:login')
