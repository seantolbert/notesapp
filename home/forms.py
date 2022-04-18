from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'tags']

class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'control__input', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'control__input', 'placeholder': 'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'control__input', 'placeholder': 'Last Name'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'control__input', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'control__input', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name', 'password1', 'password2']