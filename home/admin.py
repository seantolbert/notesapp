from django.contrib import admin
from .models import Note, Category, Tag

class NoteAdmin(admin.ModelAdmin):
    list_filter = ("category", "tag", "date")
    list_display = ("title", "date", "tag")

admin.site.register(Note)
admin.site.register(Category)
admin.site.register(Tag)
