from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("notes/", views.IndexPageView.as_view(), name='index'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('notes/create_note/', views.create_note, name='create_note'),
    path('notes/update_note/<int:note_id>', views.update_note, name='update_note'),
    path('notes/delete_note/<int:note_id>', views.delete_note, name='delete_note'),
    path("signup/", views.signup_page, name='signup'),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
