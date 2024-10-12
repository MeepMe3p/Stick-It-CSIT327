import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate,get_user_model
from .forms import TableCreationForm,CategoryCreationForm
from .models import Category,Board


# To handle the creation of the new board ---- processes the inout data from modal overlay in mainApp/home.html

def create_board(request):
    if request.method == 'POST':
        form = TableCreationForm(request.POST)
        if form.is_valid():
            board_name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            category = form.cleaned_data['category']
            board_type = form.cleaned_data['board_type']
            board_theme = form.cleaned_data['board_theme']
            visibility = form.cleaned_data['visibility']
            print("zfvzxvzxvzxvzxvzxv")
            board = Board.objects.create(board_name=board_name, description=description, board_type=board_type, board_theme=board_theme,category=category,visibility=visibility)
            board.save()
            form.save() 
            return redirect('success_page')  
    else:
        form = TableCreationForm()
    return render(request, 'board/create_table.html',{'forms': form})

# Create your views here.
# PROGRAMMER NAME: Elijah Rei Sabay
class CreateBoardView(View):
    def get(self,request):
        print(request)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            print("waaa kaay uyaaab")
            data = list(Category.objects.all().values())
            print(data)
            
            return JsonResponse({'context':data})
        else:
            print("wa kay uyab")
            choices = Category.objects.all()
            print(choices)
            return render(request,'board/create_table.html',{'form':TableCreationForm(),'form2':CategoryCreationForm})
    
    def post(self,request):
        print(request,"THIS IS THE REQUEST")
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = request.body
            data = data.decode('utf-8')
            data = json.loads(data)

            name = data['category_name']
            desc = data['category_description']

            print(f"name : {name} desc: {desc}")
            Category.objects.create(category_name = name,category_description = desc)
            
            return JsonResponse(data, safe = False)

        else:
            form = TableCreationForm(request.POST)
            print("went here madaka")
            if form.is_valid():
                board_name = form.cleaned_data['board_name']
                description = form.cleaned_data['description']
                category = form.cleaned_data['category']
                privacy_settings = form.cleaned_data['privacy_settings']
            
                cat = Board.objects.create(board_name = board_name, description = description, category = category,privacy_settings=privacy_settings)
                cat.save()
                cat.users.add(request.user.id)
                # cat.save
                return redirect("note:home")
            print(form.is_valid(),' I DONT THINK SO')
            return render(request,'board/create_table.html',{'form':TableCreationForm()})


# https://stackoverflow.com/questions/69961299/how-to-return-ajax-response-as-well-as-redirection-in-the-views-py-django : redirecting jsonresponese
class PracticeView(View):
    def get(self, request, *args, **kwargs):
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                print("hello there")
                data = Category.objects.all()
                return JsonResponse(data)
            print("aaaaaaaaa")
            return render(request, 'practiceAjax.html',{'form':CategoryCreationForm()})
    
    def post(self,request, *args, **kwargs):
        data = request.body
        data = data.decode('utf-8')
        data = json.loads(data)

        name = data['category_name']
        desc = data['category_description']

        print(f"name : {name} desc: {desc}")
        Category.objects.create(category_name = name,category_description = desc)
        # data = Category.objects.all()
        # return render(request, 'practiceAjax.html',{'form':CategoryCreationForm()})
        
        return JsonResponse(data, safe = False)
        # {'message':'data'} is the data sent
