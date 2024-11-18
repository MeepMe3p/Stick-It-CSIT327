from django import forms
from django.contrib.auth.models import User
from .models import Board,Category

class TableCreationForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label=None,widget=forms.Select(attrs={
        'onchange':'handleCategoryChange()'
    }))
    new_category = forms.CharField(required=False,max_length = 25,widget=forms.TextInput(attrs={
        "id":'new-category',
        "placeholder":"Enter category name",
        # "style":'display:none'
    }))
    new_description = forms.CharField(required=False,max_length=100,widget=forms.Textarea(attrs={
        "id":'new-desc',
        "placeholder":"Enter category description",
        # "style":'display:none'

    }))



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom choices
        self.fields['category'].choices = [
            ('', 'Select...'), 
            ('create-new', 'Create new...'), 
        ] + list(self.fields['category'].choices) 
        
        
        
    class Meta:
        model = Board
        fields = ["board_name","description","category","board_type","board_theme","visibility"]
    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super(TableCreationForm, self).__init__(*args, **kwargs)
            
        if is_update:
            self.fields.pop('board_type')


    

    
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