from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

#from ckeditor.fields import RichTextField
#from django_quill.fields import QuillField

# Create your models here.

class Page(models.Model):
    page_heading = models.CharField(max_length=30)
    page_content = RichTextField(blank=True, null=True)
    #page_slug = models.CharField(max_length=30, null=False)
    page_meta_title = models.CharField(max_length=30)
    page_meta_description= models.TextField(max_length=300)
    page_canonical_url = models.CharField(max_length=30)

    def __str__(self):
        return self.page_heading