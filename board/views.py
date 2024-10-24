import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate,get_user_model
from .forms import TableCreationForm,CategoryCreationForm
from django.contrib.auth.models import User
from .models import Category,Board
from django.views.generic import UpdateView
# To handle the creation of the new board ---- processes the inout data from modal overlay in mainApp/home.html

def create_board(request):
    print("called hereee comeon ")
    form = TableCreationForm(request.POST,request=request)
    # print(request.POST)

    if(request.user.is_authenticated):
        print("USER IS LOGGED IN", request.user)
    else:
        print("not logged in")
    if form.is_valid():
        
        board = form.save(commit=False)
        print(form.cleaned_data)
        board.board_name = form.cleaned_data['board_name']
        board.description = form.cleaned_data['description']
        board.category = form.cleaned_data['category']
        board.board_type = form.cleaned_data['board_type']
        board.board_theme = form.cleaned_data['board_theme']
        board.visibility = form.cleaned_data['visibility']

       
        try:
            users = form.cleaned_data['users']

            print(users)
            userCount = len(users)   # Check if users is empty or None
            if userCount == 0:
                userCount = 1
            else:
                userCount+=1

            print(f"User count: {userCount}")
        except KeyError:
            userCount = 1
            

        board.owner = User.objects.get(pk=request.user.id)
        # print("board owner: ",board.owner)
        print("it is valid go here")
        board.save()
        print(f"name: {board.board_name} board id: {board.id}")

        userboard = Board.objects.get(pk = board.id)
        # userboard.users.add(request.user.id) NOTE: wont work yet idk if join ni or nah
        userboard.user_count = userCount


        
        userboard.save()
        print(userboard)
        form.save() 
        # return redirect('board:create_board')  
    print(form.errors)

# Create your views here.
# PROGRAMMER NAME: Elijah Rei Sabay
class CreateBoardView(View):
        
    def get(self,request):
        print(request)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = list(Category.objects.all().values())
            print(data)
            
            return JsonResponse({'context':data})
        else:
            choices = Category.objects.all()
            # print(choices.count()+'aaa')
            context = {
                'form':TableCreationForm(request = request),
                'form2':CategoryCreationForm,
                'category':choices,
            }
            return render(request,'board/create_table.html',context)
            # return JsonResponse(context)
            # return context
    def get_context(self):
        choices = Category.objects.all()
        print(choices.count())
        context = {
            'form':TableCreationForm(request=self.request),
            'form2':CategoryCreationForm(),
            'category':choices
        }
        return context
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
            form = TableCreationForm(request.POST,request=request,)
            print("went here madaka")
            if form.is_valid():
                board_name = form.cleaned_data['board_name']
                description = form.cleaned_data['description']
                category = form.cleaned_data['category']
                privacy_settings = form.cleaned_data['privacy_settings']
            
                cat = Board.objects.create(board_name = board_name, description = description, category = category,privacy_settings=privacy_settings)
                cat.save()
                cat.users.add(request.user.id)
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
class UpdateBoard(View):
    def get(self,request,pk):
        board = Board.objects.get(pk=pk)
        context = {
            "board":board,
            "form": TableCreationForm(instance = board,request=request,board = board),
        }
        return render(request,'board/update_table.html',context)
    
    def post(self,request,pk):
        board = Board.objects.get(pk=pk)
        form = TableCreationForm(request.POST,  instance = board,request=request)
        
        if form.is_valid():
            remove_users = request.POST.getlist("remove_users")
            print("the users are",remove_users)

            if remove_users:
                board.users.remove(*remove_users)

            board.board_name = form.cleaned_data['board_name']
            board.description = form.cleaned_data['description']
            board.board_type = form.cleaned_data['board_type']
            board.visibility = form.cleaned_data['visibility']
            board.board_theme = form.cleaned_data['board_theme']
            board.category = form.cleaned_data['category']

            board.save()

            
            # form.save()
        print(form.errors)
        return redirect('mainApp:home')



