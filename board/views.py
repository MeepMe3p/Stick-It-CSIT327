import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login,authenticate,get_user_model
from .forms import TableCreationForm,CategoryCreationForm
from .models import Category,Board, ProjectBoard, SimpleBoard
from django.contrib.auth.decorators import login_required
from mainApp.utils import get_user_initials


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
        print("this is form:" ,form.data)
 
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
                return render(request, 'board/my_board.html', {'form': form, 'categories': categories})
            
            print("selected collabs: ",collaborators )
            
            if collaborators:
                for users in collaborators:
                    print(users)
                    board.users.add(users)

            board.users.add(request.user)
            board.user_count = board.users.count()
            # board.save()
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
    initials = get_user_initials(request.user)
    context = {
        'boards': boards,
        'initials' : initials,
        'boards': boards,
        'categories': categories,
        # 'selected_category': category,
    }
    return render(request,'mainApp/home.html',context)
    
@login_required
def filter_boards_by_category(request, category_slug):
    category = get_object_or_404(Category, category_slug=category_slug)
    boards = Board.objects.filter(category=category)
    categories = Category.objects.all()  
    initials = get_user_initials(request.user)

    return render(request, 'mainApp/home.html', {
        'initials' : initials,
        'boards': boards,
        'categories': categories,
        'selected_category': category,
    })

@login_required
def update_board(request,pk):
    board = Board.objects.get(pk=pk)
    category = Category.objects.all()
    users_remove = board.users.all()
    users_add = Board.objects.exclude(id__in = users_remove.values_list('id',flat=True))
    initials = get_user_initials(request.user)
    context = {
        'initials' : initials,
        'board':board,
        'categories':category,
        'add':users_add,
        'remove':users_remove,
    }
    return render(request,'board/update_board.html',context)
#