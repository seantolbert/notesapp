from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    template_name = 'home/index.html'
    model = Note
    ordering = ['-date']
    context_object_name = 'notes'

def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)
    return render(request, "home/detail.html", {"note": note})

class NoteCreate(CreateView, LoginRequiredMixin):
    model = Note
    fields = ["title", "text", "category", "tag"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class NoteUpdate(UpdateView, LoginRequiredMixin):
    model = Note
    fields = ["title", "text", "category", "tag"]

class QuoteDelete(DeleteView, LoginRequiredMixin):
    model = Note
    success_url = '/notes/'

def signup(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            error_message = "Invalid signup - Please try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)