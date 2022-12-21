from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from django.shortcuts import get_object_or_404

# Create your views here.

def hello_world(request):
    return HttpResponse("hello")
    

def all_pages(request):
    # Model.object.all() to 
    p = Page.objects.all()
    context = {'p':p}
    print(context)
    return render (request,'page-details.html', context)

def page_details(request,pk):
    p = Page.objects.get(pk=pk)
    context = {'p':p}
    return render (request,'home.html',context )
