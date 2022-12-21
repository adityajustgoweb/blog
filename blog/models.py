from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30, default='')
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = RichTextField(blank=True, null=True)
    author = models.ForeignKey(Author ,on_delete=models.CASCADE, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    meta_title = models.CharField(max_length=30, default='')
    meta_description = models.TextField(max_length=100, default='')
  
    def __str__(self):
        return self.title