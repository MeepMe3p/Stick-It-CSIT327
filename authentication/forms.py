from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django import forms
from datetime import date


# PROGRAMMER NAME: ELIJAH REI SABAY
# test2user - secondpassword
class StickItLoginForm(forms.Form):
    email = forms.EmailField(
        label = "Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter email',
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        label="Enter Password", 
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter password',
            'class': 'form-control',
            'height': '40px',
        })
    )

    class Meta:
        model = User
        fields = ['email','password']

class StickItUserCreationForm(UserCreationForm):
    
    # Disables the: 
    # https://stackoverflow.com/questions/78850636/what-is-password-based-authentication-in-the-usercreationform-in-django-and-how
    usable_password = None
    
    email = forms.EmailField(required=True, label="")
    first_name = forms.CharField(max_length=30, required=True, help_text="")
    last_name = forms.CharField(max_length=30, required=True, help_text="")

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'birth_date')
        fields = ('password1', 'password2', 'email', 'first_name', 'last_name')
    
    # This method checks if the email entered by the user already exists in the database.
    def clean_email(self):
        email = self.cleaned_data.get('email') #  Django's initial validation
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with that email already exists.")
        return email
    
    #  This method checks if the first name contains only alphabetic characters.
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name') #  Django's initial validation
        if not first_name.isalpha():
            raise forms.ValidationError("First name should only contain letters.")
        return first_name
    
    # This method checks if the last name contains only alphabetic characters, similar to the clean_first_name method.
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name') #  Django's initial validation
        if not last_name.isalpha():
            raise forms.ValidationError("Last name should only contain letters.")
        return last_name
    
    
    def __init__(self, *args, **kwargs):
        super(StickItUserCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        """
        Django’s built-in UserCreationForm automatically provides reasonable defaults for help text and validation rules, 
        so you typically don’t need to manually set them unless you have specific requirements.
        e.g. bootstrap design
        """

        # self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        # self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
        
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''
        
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        
    def save(self, commit=True):

        """
        commit=True: Saves the instance to the database immediately.
        commit=False: Creates the instance but does not save it to the database.
        You can make additional modifications before saving it.
        """
        # Create a new user instance but do not save it yet
        user = super().save(commit=False)
        # Access validated data from cleaned_data
        email = self.cleaned_data['email']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        password = self.cleaned_data['password2']

        username = f"{user.first_name} {user.last_name}"
        if(commit):
            print("Saving user to database")
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            # UserProfile.objects.create(
            #     user=user,
            #     # email=self.cleaned_data['email'],
            #     # first_name=self.cleaned_data['first_name'],
            #     # last_name=self.cleaned_data['last_name'],
            #     # birth_date=self.cleaned_data.get('birth_date', None),
            #     # phone_number=self.cleaned_data.get('phone_number', None)
            # )
        return user