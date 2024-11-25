import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views   .generic import DetailView
from django.contrib.auth import login,authenticate,get_user_model
from .forms import TableCreationForm,CategoryCreationForm
from .models import Category,Board, ProjectBoard, SimpleBoard, Notification
from django.contrib.auth.decorators import login_required
from mainApp.utils import get_user_initials
from django.contrib.auth.models import User


from authentication.models import UserProfile


# To handle the creation of the new board ---- processes the inout data from modal overlay in mainApp/home.html
@login_required(login_url='authentication:login')
def create_board(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        print("Validating form...")
        post_data = request.POST.copy()

        category_id = request.POST.get('category')
        print(f"This is the category {category_id}")
        # category = Category.objects.get(id=category_id)

        if category_id == 'create-new':
            new_category = request.POST.get('new-category', '').strip()  
            print(f"This is the new category {new_category}")
            if new_category:
                category, created = Category.objects.get_or_create(category_name=new_category)
                # print(f"Category instance: {category}")
                post_data['category'] = category.id
                print(f"Category instance: ")

        else:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                print("Invalid category selected.")
                return render(request, 'board/my_board.html', {'form': form, 'categories': categories})
            
        form = TableCreationForm(post_data)
        # print("this is form:" ,form.data)
 
        if form.is_valid():
            print("Form is valid")
            board_name = form.cleaned_data['board_name']
            description = form.cleaned_data['description']
            board_type = form.cleaned_data['board_type']
            board_theme = form.cleaned_data['board_theme']
            visibility = form.cleaned_data['visibility']

            collaborators = request.POST.getlist('collaborators')

            if board_type == 'project':
                board = ProjectBoard.objects.create(
                    board_name=board_name,
                    description=description,
                    board_type=board_type,
                    board_theme=board_theme,
                    category=category,
                    visibility=visibility,
                    creator=request.user,
                    progress=0  
                )
            elif board_type == 'simple':
                board = SimpleBoard.objects.create(
                    board_name=board_name,
                    description=description,
                    board_type=board_type,
                    board_theme=board_theme,
                    category=category,
                    visibility=visibility,
                    creator=request.user
                )
            else:
                print("Invalid board type.")
                # return render(request, 'board/my_board.html', {'form': form, 'categories': categories})
                return redirect('note:note', board=board.board_name)
            
            print("selected collabs: ",collaborators )
            
            if collaborators:
                for users in collaborators:
                    # print(users)
                    notif = Notification.objects.create(
                        user_sender = request.user,
                        user_receiver = User.objects.get(pk=users),
                        board = board,
                        notif_type = 'invite',
                        message = f'You have been invited in {board.board_name}. Accept?')
                    # board.users.add(users)

            board.users.add(request.user)
            board.user_count = board.users.count()
            board.save()
            # form.save() 
            # return redirect('board:render_board') 
            return redirect('note:note', board=board.board_name)

        else:
            print("Form errors:", form.errors) 
    else:
        form = TableCreationForm()
        form.fields['category'].queryset = categories
    return render(request, 'board/my_board.html', {'form': form, 'categories': categories})


@login_required(login_url='authentication:login')
def render_board(request):
    user_initials = get_user_initials(request.user)
    return render(request, 'board/my_board.html', {'user_initials': user_initials})

# ako giusab cuz nahan ko name ang nasa url
# @login_required(login_url='authentication:login')
# def filter_boards_by_category(request, category_id):
#     category = get_object_or_404(Category, id=category_id)
#     boards = Board.objects.filter(category=category)
#     categories = Category.objects.all()  
#     initials = get_user_initials(request.user)

#     return render(request, 'mainApp/home.html', {
#         'initials' : initials,
#         'boards': boards,
#         'categories': categories,
#         'selected_category': category,
#     })

def all_boards(request):
    boards = Board.objects.all()
    categories = Category.objects.all()
    return render(request, 'board/board_home.html', {'boards': boards, 'categories': categories})


# ej added
@login_required(login_url='authentication:login')
def filter_owner(request):
    boards = Board.objects.filter(users = request.user)
    categories = Category.objects.all()  
    notifs = Notification.objects.all()
    initials = get_user_initials(request.user)
    context = {
        'boards': boards,
        'initials' : initials,
        'boards': boards,
        'categories': categories,
        'notifications':notifs,
    }
    return render(request,'mainApp/home.html',context)
    
@login_required
def filter_boards_by_category(request, category_slug, template_name='mainApp/home.html'):
    user = request.user 
    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = None 
    
    # all_categories = Category.objects.all()
    category = get_object_or_404(Category, category_slug=category_slug)
    if template_name == 'mainApp/home.html':
        boards = Board.objects.filter(category=category)
        categories = Category.objects.all()
        count = boards.count()
    else:
        boards = Board.objects.filter(creator=user, category=category)
        categories = Category.objects.filter(board__creator=user).distinct()
        count = boards.count()
    initials = get_user_initials(request.user)
    notifs = Notification.objects.all()

    return render(request, template_name, {
        'initials' : initials,
        'user_profile': user_profile,
        'boards': boards,
        'count' : count,
        # 'all_categories' : all_categories,
        'categories': categories,
        'selected_category': category,
        'notifications':notifs,
    })

@login_required
def update_board(request,pk):
    if request.method == 'POST':
        form = TableCreationForm(request.POST,is_update =True)
        if form.is_valid():
            # print(form.data)
            board = Board.objects.get(pk=pk)
   

            board.board_name = form.cleaned_data['board_name']
            board.category = form.cleaned_data['category']
            board.description = form.cleaned_data['description']
            board.board_theme = form.cleaned_data['board_theme']
            board.visibility = form.cleaned_data['visibility']

            added = request.POST.getlist('add_user')
            removed = request.POST.getlist('remove_user')

            if added:
                for users in added:
                    # print(users)
                    notif = Notification.objects.create(
                        user_sender = request.user,
                        user_receiver = User.objects.get(pk=users),
                        board = board,
                        notif_type = 'invite',
                        message = f'You have been invited in {board.board_name}. Accept?')
                    
                    # print(notif.user_receiver)
                    # board.users.add(users)
            if removed:
                for users in removed:
                    # print(users)
                    
                    notif = Notification.objects.create(
                        user_sender = request.user,
                        user_receiver = User.objects.get(pk=users),
                        board = board,
                        notif_type = 'remove',
                        message = f'You have been removed in {board.board_name}')
                    
                    board.users.remove(users)
            board.save()

        else:
            print(form.errors)
    
    board = Board.objects.get(pk=pk)
    category = Category.objects.all()
    owner = board.creator
    users_remove = board.users.all().exclude(pk=owner.pk)
    users_add = User.objects.all().exclude(id__in=users_remove).exclude(is_staff=True).exclude(id=owner.pk)
    
    notifs = Notification.objects.all()

    # print(users_add,"asddead")
    initials = get_user_initials(request.user)
    context = {
        'initials' : initials,
        'board':board,
        'categories':category,
        'add':users_add,
        'remove':users_remove,
        'notifications':notifs,
    }
    return render(request,'board/update_board.html',context)

@login_required
def respond_invite(request,pk):
    # print("went hereeeeee")
    # print(request.POST.get('yes'))
    notif = Notification.objects.get(pk=pk)
    notif.has_responded = True
    if request.POST.get('accept'):
        board = notif.board
        print(notif)
        print(board)
        board.users.add(request.user)
        Notification.objects.create(
            user_sender = request.user,
            user_receiver = notif.user_sender,
            board = board,
            notif_type = 'accepted',
            message = f'{request.user.username} has accepted your invite in {board.board_name}')

    elif request.POST.get('decline'):
        print("no clicked")
        board = notif.board

        Notification.objects.create(
            user_sender = request.user,
            user_receiver = notif.user_sender   ,
            board = board,
            notif_type = 'decline',
            message = f'{request.user.username} has rejected your invite to join {board.board_name}')
    print("T F: ",notif.has_responded)
    notif.save()
    return redirect('mainApp:home')  
@login_required
def join_board(request,board_id):
    board = Board.objects.get(pk=board_id)
    print(board.board_name)
    notif = Notification.objects.create(
        user_sender = request.user,
        user_receiver = board.creator,
        board = board,
        notif_type = 'join',
        message = f'{request.user.username} would like to join {board.board_name}')
    print(f'{request.user.username} would like to join {board.board_name}')     
    # notif.save()
    return redirect("mainApp:home")
@login_required
def respond_join_request(request,pk):
    notif = Notification.objects.get(pk=pk)
    notif.has_responded = True
    board = notif.board
    if request.POST.get('accept'):
        print(notif)
        print(board)
        board.users.add(notif.user_sender)
        Notification.objects.create(
        user_sender = request.user,
        user_receiver = notif.user_sender,
        board = board,
        notif_type = 'accepted',
        message = f'{request.user.username} accepted your request to join {board.board_name}')
        print("went herewwwwwwwwwwwwwwwwww")
    elif request.POST.get('decline'):
        # print("no clicked")

        Notification.objects.create(
        user_sender = request.user,
        user_receiver = notif.user_sender,
        board = board,
        notif_type = 'decline',
        message = f'{request.user.username} rejected your request to join {board.board_name}')
        print("went herewwwwwwwwwwwwwwwwww")
    print("T F: ",notif.has_responded)
    notif.save()
    return redirect('mainApp:home')  
    

class BoardDetailView(DetailView):
    model = Board
    template_name = 'board/my_board.html'
    context_object_name = 'board'

    def get_object(self):
        board = super().get_object()
        return board
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        board = self.get_object()
        initials = get_user_initials(board.creator)
        
        context['initials'] = initials
        return context
#


# oh diba sheesshhhhh muredirect na sa note
def go_to_effing_board(request,pk):
    board = Board.objects.get(pk=pk)
    return redirect('note:note', board=board.board_name)
