from django import forms
from django.contrib.auth.models import User
from authentication.models import UserProfile

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=50, required=True)

    class Meta:
        model = UserProfile
        fields = ['birthdate','description']
    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email') #  Django's initial validation
    #     if User.objects.filter(email=email).exists():
    #         print("Email already exists")
    #         raise forms.ValidationError("A user with that email already exists.")
    #     return email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance.user  # Get the user instance linked to this profile

        # Check if another user with the same email exists
        if User.objects.filter(email=email).exclude(pk=user.pk).exists():
            raise forms.ValidationError("A user with that email already exists.")
        
        return email

    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile.save()
        return profile
    

class SocialLinksEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['facebook_link','linkedin_link','twitter_link']
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile

    # facebook_link = forms.CharField(max_length=100)
    # linkedin_link = forms.CharField(max_length=100)
    # twitter_link = forms.CharField(max_length=100)