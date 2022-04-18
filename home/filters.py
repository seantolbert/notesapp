from .models import *
from django import forms
import django_filters 
from django.db.models import Q


# class NoteFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr="icontains", label='Title')
#     text = django_filters.CharFilter(lookup_expr="icontains", label='Text')
    
#     class Meta:
#         model = Note
#         fields = ['title', 'text']

class NoteFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='custom_filter', 
        label='',
        widget=forms.TextInput(attrs={
            'class': 'search__input', 
            'placeholder': 'search...'
            })
        )

    class Meta:
        model = Note
        fields = ['q']


    def custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) | Q(text__icontains=value)
        )
