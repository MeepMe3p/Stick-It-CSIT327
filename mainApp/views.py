from django.shortcuts import render,redirect
from django.views import View
from board.models import Board, Category
from board.views import create_board 
from django.contrib.auth.models import User
from board.forms import TableCreationForm, CategoryCreationForm

# Create your views here.
class Home(View):
    def get(self,request):
        choices = Category.objects.all()
        users = User.objects.all().filter().exclude(pk=request.user.id)
        print(choices.count())
        context = {
            'form':TableCreationForm(),
            'form2':CategoryCreationForm,
            'category':choices,
            'users':users,
        }
        return render(request, 'mainApp/home.html',context)
    def post(self,request):
        create_board(request)

        return redirect('board:create_board')  


# def home(request):
#     return render(request, 'mainApp/home.html',context)

def myBoards(request):
    return render(request, 'mainApp/my_boards.html')

def profile(request):
    return render(request, 'mainApp/profile.html')