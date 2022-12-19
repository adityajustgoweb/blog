from django.db import models

# Create your models here.

class Author(models.Model):
    Author_name = models.CharField(max_length=30)
    Author_bio = models.CharField(max_length=30)
    Author_pic = models.ImageField(upload_to='uploads/')


class Post(models.Model):
    Post_title = models.CharField(max_length=30)
    Post_description = models.CharField(max_length=30)
  