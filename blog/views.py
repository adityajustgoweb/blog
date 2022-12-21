from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def hello_blog(request):
    return HttpResponse("Hello Blog")


def handleSignup(request):
    if request.method=='POST':
        #get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        # Create the user
        member = User.objects.create_user(username,email, pass1)
        member.first_name=fname
        member.last_name=lname
        member.phone_num=phone
        member.save()
        messages.success(request, "Account Created")
        return HttpResponse("User Created")
    
    else:
        return render(request, 'signup.html')


