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
<<<<<<< Updated upstream
    return render(request, 'board/create_table.html',{'forms': form})
=======
        form.fields['category'].queryset = categories
    
    return render(request, 'board/my_board.html', {'form': form, 'categories': categories})
>>>>>>> Stashed changes

# Create your views here.
# PROGRAMMER NAME: Elijah Rei Sabay
# class CreateBoardView(View):
    # def get(self,request):
    #     print(request)
    #     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #         data = list(Category.objects.all().values())
    #         print(data)
    #         return JsonResponse({'context':data})
    #     else:
    #         choices = Category.objects.all()
    #         print(choices)
    #         return render(request,'board/my_board.html',{'form':TableCreationForm(),'form2':CategoryCreationForm})
    
    # def post(self,request):
    #     print(request,"THIS IS THE REQUEST")
    #     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    #         data = request.body
    #         data = data.decode('utf-8')
    #         data = json.loads(data)

    #         name = data['category_name']
    #         desc = data['category_description']

    #         print(f"name : {name} desc: {desc}")
    #         Category.objects.create(category_name = name,category_description = desc)
            
    #         return JsonResponse(data, safe = False)

    #     else:
    #         form = TableCreationForm(request.POST)
    #         if form.is_valid():
    #             board_name = form.cleaned_data['board_name']
    #             description = form.cleaned_data['description']
    #             category = form.cleaned_data['category']
    #             privacy_settings = form.cleaned_data['privacy_settings']
            
    #             cat = Board.objects.create(board_name = board_name, description = description, category = category,privacy_settings=privacy_settings)
    #             cat.save()
    #             cat.users.add(request.user.id)
    #             return redirect("note:home")
    #         return render(request,'board/my_board.html',{'form':TableCreationForm()})


@login_required(login_url='authentication:login')
def render_board(request):
    user_initials = get_user_initials(request.user)
    return render(request, 'board/my_board.html', {'user_initials': user_initials})

@login_required(login_url='authentication:login')
def filter_boards_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    boards = Board.objects.filter(category=category)
    categories = Category.objects.all()  
    initials = get_user_initials(request.user)

    return render(request, 'mainApp/home.html', {
        'initials' : initials,
        'boards': boards,
        'categories': categories,
        'selected_category': category,
    })