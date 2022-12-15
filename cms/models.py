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

"""

class Department(models.Model):
    department_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.department_name

class Roles(models.Model):
    role_name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.role_name

class Employee(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    salary = models.IntegerField(default=12000)
    bonus = models.IntegerField(default=2000)
    phone = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    hire_date = models.DateTimeField ()
    #bio = RichTextField(blank=True, null=True)
    bio = QuillField()


    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

"""