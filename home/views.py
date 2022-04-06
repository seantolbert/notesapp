import re
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, NoteForm
from .models import Note


class HomePageView(ListView):
    template_name = 'home/home.html'
    model = Note
    ordering = ['-date']
    context_object_name = 'notes'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class IndexPageView(ListView):
    template_name = 'notes/index.html'
    model = Note
    ordering = ['-date']
    context_object_name = 'notes'

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, "home/detail.html", {"note": note})

def create_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'notes/note_form.html', context)

def update_note(request, note_id):
    note = Note.objects.get(id=note_id)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'notes/note_form.html', context)

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    context = {'note': note}
    return render(request, 'notes/delete.html', context)

def signup_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('login')
        else:
            messages.error(request, 'User signup failed, please try again')
    context = {'form': form}
    return render(request, 'registration/signup.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')