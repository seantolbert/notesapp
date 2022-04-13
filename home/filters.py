from dataclasses import fields
from .models import *
import django_filters 


class NoteFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains", label='Title')
    text = django_filters.CharFilter(lookup_expr="icontains", label='Text')
    
    class Meta:
        model = Note
        fields = ['title', 'text']
        
