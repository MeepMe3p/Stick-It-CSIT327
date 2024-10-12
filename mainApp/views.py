from django.shortcuts import render
from board.models import Board

# Create your views here.
def home(request):
    # if request.method == 'GET':
    #     board = Board.objects.all()
    return render(request, 'mainApp/home.html')

def myBoards(request):
    return render(request, 'mainApp/my_boards.html')

def profile(request):
    return render(request, 'mainApp/profile.html')