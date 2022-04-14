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
from .filters import NoteFilter


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'home/home.html'
    model = Note
    ordering = ['-date']
    context_object_name = 'notes'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

class IndexPageView(LoginRequiredMixin, ListView):
    template_name = 'notes/index.html'
    model = Note
    ordering = ['-date']
    context_object_name = 'notes'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, "home/detail.html", {"note": note})

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text', 'category', 'tags']
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# def create_note(request):
#     form = NoteForm()
#     if request.method == 'POST':
#         form = NoteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {'form': form}
#     return render(request, 'notes/note_form.html', context)

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'text', 'category', 'tags']
    login_url = 'login'
    redirect_field_name = 'redirect_to'

# def update_note(request, note_id):
#     note = Note.objects.get(id=note_id)
#     form = NoteForm(instance=note)
#     if request.method == 'POST':
#         form = NoteForm(request.POST, instance=note)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     context = {'form': form}
#     return render(request, 'notes/note_form.html', context)

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    success_url = "/"
    login_url = 'login'
    redirect_field_name = 'redirect_to'

# def delete_note(request, note_id):
#     note = Note.objects.get(id=note_id)
#     if request.method == 'POST':
#         note.delete()
#         return redirect('home')
#     context = {'note': note}
#     return render(request, 'notes/delete.html', context)

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