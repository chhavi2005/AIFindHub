from django.forms import ModelForm
from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields =['username', 'email', 'password1','password2']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone','desc']