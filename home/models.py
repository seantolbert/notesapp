from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

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
    text = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, related_name="notes")
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("note_detail", kwargs={"note_id": self.id})

