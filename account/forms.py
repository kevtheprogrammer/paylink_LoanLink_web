from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

 
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'email', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2', 
        ]


class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'avatar',
            'email', 
            'first_name', 
            'last_name', 
            # 'dob', 
            'nrc', 
            'phone', 
            'location', 
            'country',          
        ]
