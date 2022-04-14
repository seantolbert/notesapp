from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'tags']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", 'first_name', 'last_name', 'email', 'password1', 'password2']