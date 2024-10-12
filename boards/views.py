import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
# from .forms import TableCreationForm,CategoryCreationForm
from .forms import TableCreationForm,CategoryCreationForm
from boards.models import Category,Board

def create_board(request):
    print(request)
    # if request.method == "GET":
    #     return render()
    if request.method == 'POST':

        form = TableCreationForm(request.POST)
        print(form.is_valid(),"fricc")

        if form.is_valid():
            print("zxfvcbxncbxbc")

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
        print("di valud")
    return render(request, 'boards/create_table.html',{'forms': form})

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
            # print("went here madaka")
            if form.is_valid():
                board_name = form.cleaned_data['board_name']
                description = form.cleaned_data['description']
                category = form.cleaned_data['category']
                privacy_settings = form.cleaned_data['privacy_settings']
            
                cat = Board.objects.create(board_name = board_name, description = description, category = category,privacy_settings=privacy_settings)
                cat.save()
                cat.users.add(request.user.id)
                # cat.save
                return redirect("stickit:home")
            print(form.is_valid(),' I DONT THINK SO')
            return render(request,'board/create_table.html',{'form':TableCreationForm()})