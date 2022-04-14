from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name='home'),
    path("notes/", views.IndexPageView.as_view(), name='index'),
    path('notes/<int:note_id>/', views.note_detail, name='note_detail'),
    path('notes/create_note/', views.NoteCreate.as_view(), name='create_note'),
    path('notes/update_note/<int:pk>', views.NoteUpdate.as_view(), name='update_note'),
    path('notes/delete_note/<int:pk>', views.NoteDelete.as_view(), name='delete_note'),
    path("signup/", views.signup_page, name='signup'),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
