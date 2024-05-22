from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Feedback
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("homePage")

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, "User not exists")
            return redirect('LoginPage')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request ,user)
            messages.success(request, "You are now logged in :) ")
            return redirect("homePage")

        else:
            messages.error(request, "Username or password incorrect :( ")
            # return HttpResponse("Username or password incorrect")
            return redirect("LoginPage")

    # return HttpResponse("LoginPage page")
    return render(request,"Users/login.html")


def registerUser(request):
    # return HttpResponse("Register page")
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User(first_name=name,username=username,email=email,password=password)
        user.username = user.username.lower()
        try :
            user_db = User.objects.get(username=username)
            print(user_db.username == username)
            print("User already exists")
            messages.error(request, "Username already exists :( ")
        except Exception as e :
            print(username)
            user.set_password(password)
            user.save()
            messages.success(request,"User successfully created :) ")

    return render(request,"Users/register.html")

@login_required(login_url="LoginPage")
def feedback(request):
    if request.method == "POST":
        email = request.POST['email']
        user_feedback = request.POST['user_feedback']
        name = request.user.username
        user_id = request.user
        feedback = Feedback(name=name,email=email,user_feedback=user_feedback,username=user_id)
        feedback.save()
        messages.success(request,"We got your feedback ")
    # return HttpResponse("Feeback page")
    username = request.user.username
    context = {
        'username':username
    }
    return render(request,"Users/feedback.html", context)

def logoutUser(request):
    logout(request)
    messages.info(request, "Logout successfull :)")
    return redirect('LoginPage')