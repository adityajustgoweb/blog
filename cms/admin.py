from django.contrib import admin
from .models import Page
from ckeditor.widgets import CKEditorWidget
#admin.py

# Register your models here.

admin.site.register(Page)
