from django.shortcuts import render
from board.models import Board, ProjectBoard, SimpleBoard
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .utils import get_user_initials
from board.models import Category
from authentication.models import UserProfile
from .forms import ProfileEditForm, SocialLinksEditForm


@login_required(login_url='authentication:login')
def home(request):
    categories = Category.objects.all()
    boards = Board.objects.all()
    projectboards = ProjectBoard.objects.all()
    simpleboards = SimpleBoard.objects.all()
    # if request.method == 'GET':
    #     board = Board.objects.all()
    print(request.user.first_name)
    print(request.user.last_name)
    initials = get_user_initials(request.user)
    context = {
        'initials': initials, 
        'categories': categories,
        'boards': boards,
        'projectboards' : projectboards,
        'simpleboards' : simpleboards
    }
    print(f"This is context {context}")
    return render(request, 'mainApp/home.html', context)

@login_required(login_url='authentication:login')
def my_space(request):
    initials = get_user_initials(request.user)
    # boards = Board.objects.all()
    # categories = Category.objects.all()
    user = request.user
    boards = Board.objects.filter(creator=user)
    categories = Category.objects.filter(board__creator=user).distinct()

    count = boards.count()
    print(f"Number of boards current user has: {count}")

    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = None 
    
    context = {
        'initials': initials,
        'user_profile': user_profile,
        'categories': categories,
        'boards': boards,
        'count' : count,   
        'show_my_boards_section': True if request.GET.get('show') == 'my-boards' else False
    }
    return render(request, 'mainApp/my_space.html', context)

def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        print("Validating editing form...")
        form = ProfileEditForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            print("Editing form is valid. Proceeding...")
            form.save()
            return redirect('mainApp:my_space')
    else:
        form = ProfileEditForm(instance=profile, user=request.user)
    return render(request, 'mainApp/my_space.html', {'form': form})


def edit_social_links(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        print("Validating editing social links form...")
        form = SocialLinksEditForm(request.POST, instance=profile)
        if form.is_valid():
            print("Social Links Editing form is valid. Proceeding...")
            form.save()
            return redirect('mainApp:my_space')
    else:
        form = SocialLinksEditForm(instance=profile)
    return render(request, 'mainApp/my_space.html', {'form': form})