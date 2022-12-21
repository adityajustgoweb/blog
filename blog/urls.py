from django.urls import path
from . import views 

urlpatterns = [
    
    path('blog', views.hello_blog, name ='blog'),
    path('signup', views.handleSignup, name ='handlesignup')

]

