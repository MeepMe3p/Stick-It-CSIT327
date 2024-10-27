from django import forms
from django.contrib.auth.models import User
from .models import Board,Category

class TableCreationForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ["board_name","description","category","board_type","board_theme","visibility"]
    

    
# https://forum.djangoproject.com/t/how-to-create-dynamic-modals-popups-in-template/8338/2
class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "category_description"]

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        if Category.objects.filter(category_name = category_name).exists():
            raise forms.ValidationError("A category with that name already exists.")
        return category_name
