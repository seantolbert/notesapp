from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    label = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return self.label

class Note(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)
    text = RichTextField(blank = True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="notes")
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"note_id": self.id})

