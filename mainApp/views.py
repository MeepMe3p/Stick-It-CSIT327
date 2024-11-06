from django.shortcuts import render
from board.models import Board, ProjectBoard, SimpleBoard, Notification
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .utils import get_user_initials
from board.models import Category
from authentication.models import UserProfile
from .forms import ProfileEditForm
from django.contrib.auth.models import User


@login_required(login_url='authentication:login')
def home(request):
    categories = Category.objects.all()
    boards = Board.objects.all().exclude(creator = request.user).exclude(users = request.user)
    projectboards = ProjectBoard.objects.all()
    simpleboards = SimpleBoard.objects.all()
    # notifs = Notification.objects.all()
    notifs = Notification.objects.all().filter(user_receiver = request.user)
    # ej changes
    users = User.objects.all().exclude(id = request.user.id).exclude(is_staff=True)
    #
    # if request.method == 'GET':
    #     board = Board.objects.all()
    # if notifs:
    #     for notif in notifs:
    #         print(request.user,' == ' , notif.user_receiver)
    #         print(notif)
    # else:
    #     print("empty")
    print(request.user.last_name)
    initials = get_user_initials(request.user)
    context = {
        'initials': initials, 
        'categories': categories,
        'boards': boards,
        'projectboards' : projectboards,
        'simpleboards' : simpleboards,
        'users' : users,
        'notifications':notifs,
    }
    # print(f"This is context {context}")
    return render(request, 'mainApp/home.html', context)

@login_required(login_url='authentication:login')
def my_space(request):
    initials = get_user_initials(request.user)
    # ej changes 
    # mudisplay uban nga board bisag di iyaha fixed
    print(request.user.id)
    boards = Board.objects.all().filter(creator =request.user.id)
    # 
    categories = Category.objects.all()
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = None 
    context = {
        'initials': initials,
        'user_profile': user_profile,
        'categories': categories,
        'boards': boards
    }
    return render(request, 'mainApp/my_space.html', context)

def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('mainApp:my_space')
    else:
        form = ProfileEditForm(instance=profile, user=request.user)
    return render(request, 'mainApp/my_space.html', {'form': form})