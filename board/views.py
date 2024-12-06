import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views   .generic import DetailView
from django.contrib.auth import login,authenticate,get_user_model
from .forms import TableCreationForm,CategoryCreationForm
from .models import Category,Board, ProjectBoard, SimpleBoard
from django.contrib.auth.decorators import login_required
from mainApp.utils import get_user_initials
from authentication.models import UserProfile


# To handle the creation of the new board ---- processes the inout data from modal overlay in mainApp/home.html
@login_required(login_url='authentication:login')
def create_board(request):
    print("jasbdajosnfjasnfajosnfajsnfkjansfkjasnfkjanfkjansfk")
    categories = Category.objects.all()
    if request.method == 'POST':
        print("Validating form...")
        form = TableCreationForm(request.POST)

        category_id = request.POST.get('category')
        print(f"This is the category {category_id}")
        # category = Category.objects.get(id=category_id)

        if category_id == 'create-new':
            new_category = request.POST.get('new-category', '').strip()  
            print(f"This is the new category {new_category}")
            if new_category:
                category, created = Category.objects.get_or_create(category_name=new_category)
                print(f"Category instance: {category}")
        else:
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                print("Invalid category selected.")
                return render(request, 'board/my_board.html', {'form': form, 'categories': categories})

        if form.is_valid():
            print("Form is valid")
            board_name = form.cleaned_data['board_name']
            description = form.cleaned_data['description']
            board_type = form.cleaned_data['board_type']
            board_theme = form.cleaned_data['board_theme']
            visibility = form.cleaned_data['visibility']

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
                return render(request, 'board/my_board.html', {'form': form, 'categories': categories})

            board.users.add(request.user)
            board.user_count = board.users.count()
            board.save()
            # form.save() 
            return redirect('board:render_board')  
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

@login_required(login_url='authentication:login')
def filter_boards_by_category(request, category_id, template_name='mainApp/home.html'):
    user = request.user 
    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = None 
    
    # all_categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    if template_name == 'mainApp/home.html':
        boards = Board.objects.filter(category=category)
        categories = Category.objects.all()
        count = boards.count()
    else:
        boards = Board.objects.filter(creator=user, category=category)
        categories = Category.objects.filter(board__creator=user).distinct()
        count = boards.count()
    initials = get_user_initials(request.user)

    return render(request, template_name, {
        'initials' : initials,
        'user_profile': user_profile,
        'boards': boards,
        'count' : count,
        # 'all_categories' : all_categories,
        'categories': categories,
        'selected_category': category,
        # 'show_my_boards_section': True if request.GET.get('show') == 'my-boards' else False
    })

def all_boards(request):
    boards = Board.objects.all()
    categories = Category.objects.all()
    return render(request, 'board/board_home.html', {
        'boards': boards, 
        'categories': categories,
    })

def join_board(request, board_id):
    # board = Board.objects.get(id=board_id)
    board = get_object_or_404(Board, id=board_id)
    board.users.add(request.user)
    board.collaborators.add(request.user)
    board.user_count = board.users.count() 
    board.save()
    return redirect('board:board_detail', pk=board.id)

# def joined_boards(request):
#     return render(request, 'mainApp/boards.html', context)

# def shared_boards(request):
#     return render(request, 'board')

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
    