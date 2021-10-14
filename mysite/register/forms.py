from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
#modified user creation form

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Last Name')
    
    class Meta:
        model = User
        fields = ["email","first_name","last_name" , "password1", "password2"]