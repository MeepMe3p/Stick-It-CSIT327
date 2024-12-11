from django import forms
from django.contrib.auth.models import User
from authentication.models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class ProfileEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.CharField(max_length=50, required=True)

    class Meta:
        model = UserProfile
        fields = ['birthdate','description']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance.user  # Get the user instance linked to this profile

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
        user.username = user.first_name +"_"+user.last_name
        print(f"Saving profile with birthdate: {self.cleaned_data['birthdate']}")
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

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()
        return profile

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'edit-password-input'}),
        label="Old Password",
        required=True
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'edit-password-input'}),
        label="New Password",
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'edit-password-input'}),
        label="Confirm Password",
        required=True
    )

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        if not self.user.check_password(old_password):
            raise ValidationError("The old password is incorrect.")
        return old_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise ValidationError("New password and confirm password do not match.")

        return cleaned_data
