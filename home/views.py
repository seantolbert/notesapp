from django.views.generic import ListView, DetailView
from django.shortcuts import render
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