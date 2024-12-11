from django.shortcuts import render
from board.models import Board, ProjectBoard, SimpleBoard, Notification
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth import logout, get_user_model
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .utils import get_user_initials
from board.models import Category
from authentication.models import UserProfile
from .forms import ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import ChangePasswordForm
from .forms import ProfileEditForm, SocialLinksEditForm, ProfileImageForm


@login_required(login_url='authentication:login')
def home(request):
    if request.method == 'POST':
        query = request.POST.get('q')
    else:
        query = None
    categories = Category.objects.all()
    boards = Board.objects.all().exclude(creator = request.user).exclude(users = request.user)
    projectboards = ProjectBoard.objects.all()
    simpleboards = SimpleBoard.objects.all()
    notifs = Notification.objects.all().filter(user_receiver = request.user)
    users = User.objects.all().exclude(id = request.user.id).exclude(is_staff=True)
    
    print(request.user.last_name)
    initials = get_user_initials(request.user)
    user_profile = UserProfile.objects.get(user = request.user)
    # user_profile = UserProfile.objects.get(user = 3)
    if query:
        boards = boards.filter(Q(board_name__icontains=query))
    context = {
        'user_profile': user_profile,
        'initials': initials, 
        'categories': categories,
        'boards': boards,
        'users' : users,
        'projectboards' : projectboards,
        'simpleboards' : simpleboards,
        'users' : users,
        'notifications':notifs,
    }
    for asher in boards:
        print(asher.board_type)
        if asher.board_type == "project":
            print("asher is a project", asher.board_name)
    # print(f"This is context {context}")
    return render(request, 'mainApp/home.html', context)

@login_required(login_url='authentication:login')
def my_space(request):
    print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeea")
    initials = get_user_initials(request.user)
    user = request.user
    boards = Board.objects.filter(creator=user)
    categories = Category.objects.filter(board__creator=user).distinct()
    User = get_user_model()
    users = User.objects.all()
    db_categories = Category.objects.all()

    count = boards.count()
    print(f"Number of boards current user has: {count}")
    print("milk")
    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = None 
    
    context = {
        'initials': initials,
        'user_profile': user_profile,
        'categories': categories,
        'db_categories' : db_categories,
        'users' : users,
        'boards': boards,
        'count' : count,   
        # 'show_my_boards_section': True if request.GET.get('show') == 'my-boards' else False
    }
    return render(request, 'mainApp/my_space.html', context)

@login_required(login_url='authentication:login')
def profile(request):
    initials = get_user_initials(request.user)
    user = request.user
    boards = Board.objects.filter(creator=user, is_active=True)
    User = get_user_model()
    users = User.objects.all()

    count = boards.count()
    print(f"Number of boards current user has: {count}")

    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = None 
    
    context = {
        'initials': initials,
        'user_profile': user_profile,
        'users' : users,
        'boards': boards,
        'count' : count,   
    }
    return render(request, 'mainApp/profile.html', context)

@login_required(login_url='authentication:login')
def boards(request):
    initials = get_user_initials(request.user)
    user = request.user
    boards = Board.objects.filter(creator=user, is_active=True)
    User = get_user_model()
    users = User.objects.all()
    user_profile = UserProfile.objects.get(user=user)

    count = boards.count()
    # projects = []
    print(f"Number of boards current user has: {count}")
    # for board in boards:
    #     print(board.board_type)
    #     if board.board_type == "project":
    #         projects.append(board)
    print("coookieee")
    asher_projects = Board.objects.filter(board_type = "project")
    asher_projects = []
    for board in boards:
        if board.board_type == "project":
            print(board.board_name," is ",board.board_type)
            ash = ProjectBoard.objects.get(pk = board.id)
            asher_projects.append(ash)
    context = {
        'user_profile': user_profile,
        'initials': initials,
        'users' : users,
        'boards': boards,
        'count' : count, 
        'projectboards':asher_projects,  
    }
    return render(request, 'mainApp/boards.html', context)

# @login_required(login_url='authentication:login')
# def joined_boards(request):
    # initials = get_user_initials(request.user)
    # user = request.user
    # boards = Board.objects.filter(creatorc=user)
    # User = get_user_model()
    # users = User.objects.all()

    # count = boards.count()
    # print(f"Number of boards current user has: {count}")
    
    # context = {
    #     'initials': initials,
    #     'users' : users,
    #     'boards': boards,
    #     'count' : count,   
    # }
    # return render(request, 'mainApp/boards.html', context)

def collaborated_boards(request):
    initials = get_user_initials(request.user)
    user = request.user
    boards = Board.objects.filter(collaborators = user, is_active=True)
    User = get_user_model()
    users = User.objects.all()


    asher_projects = Board.objects.filter(board_type = "project")
    asher_projects = []
    count = boards.count()
    for board in boards:
        if board.board_type == "project":
            ash = ProjectBoard.objects.get(pk = board.id)
            asher_projects.append(ash)
    print("copium")
    for board in asher_projects:
        print("progress type: ",board.progress)
        # if board.board_type == "projects":
            # projects.append(board)
    
    context = {
        'initials': initials,
        'users' : users,
        'boards': boards,
        'count' : count,   
        'projectboards':asher_projects,
    }
    return render(request, 'mainApp/boards.html', context)

def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        print("Validating editing form...")
        form = ProfileEditForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            print("Editing form is valid. Proceeding...")
            form.save()
            return redirect('mainApp:profile')
    else:
        form = ProfileEditForm(instance=profile, user=request.user)

    initials = get_user_initials(request.user)
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'form': form,
        'user_profile' : user_profile,
        'initials': initials 
    }
    return render(request, 'mainApp/profile.html', context)

def profile_image(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        if request.POST["action"] == "remove":
            profile.image.delete(save=False) 
            profile.image = None
            profile.save()
            return redirect("mainApp:profile")
        elif "action" in request.POST and request.POST["action"] == "upload":
            form = ProfileImageForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect("mainApp:profile")
        else:
            form = ProfileImageForm(instance=profile)
    else:
        form = ProfileImageForm(instance=user_profile)

    initials = get_user_initials(request.user)
    user_profile = UserProfile.objects.get(user=request.user)
    context = {
        'form': form,
        'user_profile' : user_profile,
        'initials': initials 
    }
    return render(request, 'mainApp/profile.html', context)


def edit_social_links(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        print("Validating editing social links form...")
        form = SocialLinksEditForm(request.POST, instance=profile)
        if form.is_valid():
            print("Social Links Editing form is valid. Proceeding...")
            form.save()
            return redirect('mainApp:profile')
    else:
        form = SocialLinksEditForm(instance=profile)
    return render(request, 'mainApp/profile.html', {'form': form})

@login_required
def edit_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get("new_password")
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user) 
            messages.success(request, "Your password has been successfully updated.")
            return redirect("mainApp:editPassword")
    else:
        form = ChangePasswordForm(user=request.user)

    categories = Category.objects.all()
    boards = Board.objects.filter(is_active=True)
    notifs = Notification.objects.all().filter(user_receiver = request.user)
    # users = User.objects.all().exclude(id = request.user.id).exclude(is_staff=True)
    users = User.objects.all()
    print(request.user.last_name)
    initials = get_user_initials(request.user)
    user_profile = UserProfile.objects.get(user = request.user)
    context = {
        'user_profile': user_profile,
        'initials': initials, 
        'categories': categories,
        'boards': boards,
        'users' : users,
        'users' : users,
        'notifications':notifs,
    }
    return render(request, 'mainApp/home.html', context)


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.is_active = False
        user.save()

        user_boards = Board.objects.filter(creator=user)  
        user_boards.update(is_active=False)  

        logout(request)
        messages.success(request, "Your account and all associated boards have been successfully deactivated.")
        return redirect("authentication:login") 
    else:
        messages.error(request, "Invalid request.")
        return redirect("mainApp:profile")