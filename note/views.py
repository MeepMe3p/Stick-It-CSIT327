import json
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login,authenticate,get_user_model
from django.contrib import messages
from .models import Note
from django.template.context import RequestContext
from django.http import JsonResponse
class NoteView(View):
    def get(self, request):
        return render(request, 'note.html')
class NoteCreateView(View):
    def post(self, request, *args, **kwargs):
        try:
            print("Furina!")
            data = json.loads(request.body.decode('utf-8'))
            content = data.get('content')
            borderColor = data.get('borderColor')
            coordinates = data.get('coordinates')
            
            print(f"Content: {content}, Border Color: {borderColor}, Coordinates: {coordinates}")

            note = Note.objects.create(content=content, border_color=borderColor, coordinates=coordinates)

            print(note.id)
            
            return JsonResponse({'id': note.id}, status=201)

        except Exception as e:
            print(f"Error: {e}")  # Print the error message
            return JsonResponse({'error': str(e)}, status=400)
        
class NoteUpdateView(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            data = json.loads(request.body.decode('utf-8'))

            note = Note.objects.get(pk=pk)
            note_data = serialize_note(note, data)
            print(note_data)
            return JsonResponse(note_data, status=200)

        except Note.DoesNotExist:
            return JsonResponse({'error': 'Note not found'}, status=404)
        except Exception as e:
            print(f"Error: {e}")  # Print the error message
            return JsonResponse({'error': str(e)}, status=400)
        
class NoteDeleteView(View):
    def delete(self, request, pk, *args, **kwargs):
        try:
            note = Note.objects.get(pk=pk)
            note.delete()
            return JsonResponse({'message': 'Note deleted successfully'}, status=200)
        except Note.DoesNotExist:
            return JsonResponse({'error': 'Note not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        
class NoteGetView(View):
    def get(self, request, *args, **kwargs):
        notes = Note.objects.all().values('id', 'content', 'border_color', 'coordinates')
        return JsonResponse(list(notes), safe=False)
    
def serialize_note(note, data):
    # Update the note's attributes with the data received
    note.content = data.get('content', note.content)  # Use existing value if key not present
    note.border_color = data.get('border_color', note.border_color)
    note.coordinates = data.get('coordinates', note.coordinates)

    # Save the updated note to the database
    note.save()

    # Return the serialized note data
    return {
        'id': note.id,
        'content': note.content,
        'border_color': note.border_color,
        'coordinates': note.coordinates,
    }      
    

# from django.contrib.auth.views import Temp

# Create your views here.
# PROGRAMMER NAME: AVRIL NIGEL CHUA
# class RegisterService(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'register2.html', {'form': StickItUserCreationFrom()})
#     def post(self, request, *args, **kwargs):
#         if request.method == 'POST':
#             form = StickItUserCreationFrom(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request, user)
#                 messages.success(request, 'Account created successfully!')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Please correct the error below.')
#         return render(request, 'register2.html', {'form': form})
    

class LoginService(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

class HomeView(View):
    # def get()
    print("welcome home")
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')
