import re
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
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

# @login_required
class IndexPageView(ListView):
    template_name = 'notes/index.html'
    model = Note
    ordering = ['-date']
    context_object_name = 'notes'

# @login_required(login_url='login')
def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, "home/detail.html", {"note": note})

# @login_required(login_url='login')
class NoteCreate(CreateView, LoginRequiredMixin):
    model = Note
    fields = ["title", "text", "category", "tag"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# @login_required(login_url='login')
class NoteUpdate(UpdateView, LoginRequiredMixin):
    model = Note
    fields = ["title", "text", "category", "tag"]

# @login_required(login_url='login')
class QuoteDelete(DeleteView, LoginRequiredMixin):
    model = Note
    success_url = '/notes/'

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