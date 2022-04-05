from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("notes/", views.IndexPageView.as_view(), name='index'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail')
]
