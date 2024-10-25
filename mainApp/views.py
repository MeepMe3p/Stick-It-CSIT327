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
        board = Board.objects.filter(owner = request.user.id)
        print(choices.count())
        context = {
            'form':TableCreationForm(request = request),
            'form2':CategoryCreationForm,
            'category':choices,
            'boards':board,
            'loggedIn': request.user,
        }
        return render(request, 'mainApp/home.html',context)
    def post(self,request):
        create_board(request)
        return redirect('mainApp:home')  

    # to access logged in user in forms.. go to forms for le referemce
    def get_form_kwargs(self):
        print("shuba shuba")
        kwargs = super(Home, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

        


# def home(request):
#     return render(request, 'mainApp/home.html',context)

def myBoards(request):
    return render(request, 'mainApp/my_boards.html')

def profile(request):
    return render(request, 'mainApp/profile.html')