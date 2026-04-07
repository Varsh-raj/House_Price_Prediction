from django.core import validators
from django import forms
# from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class  sign_up_form(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'box', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'box', 'placeholder': 'Confirm your password'})
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Your last name'}),
            'email': forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter Your email'}),
            'username': forms.TextInput(attrs={'class': 'box', 'placeholder': 'Enter the username'}),
        }


class login_form(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'box', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'box', 'placeholder': 'Password'})