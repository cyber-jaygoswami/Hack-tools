from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homePage(request):
    # return HttpResponse("Hacker's home page")
    username = request.user.username
    context = {
        'username' : username
    }
    return render(request,"HackerHome/index.html" ,context)
