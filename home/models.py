from django.db import models

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

