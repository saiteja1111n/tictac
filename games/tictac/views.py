from django.shortcuts import render

# Create your views here.
from .models import User
from django.http import HttpResponse
from django.shortcuts import render
import json

def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User(username=username,password=password)
    user.save()
    return render(request,"login.html",{})

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.filter(username=username)
    # return HttpResponse(user)
    for a in user:
        if a.password == password:
            return render(request,"home.html",{})
        else:
            render(request,"login.html",{"message":"Login Form:(invalid credintials)"})
    return render(request,"login.html",{"message":"Login Form:(invalid credintials)"})

def loginform(request):
    return render(request,"login.html",{"message":"Login Form:"})

def registerform(request):
    return  render(request,"register.html")

def startgame(request):
    return render(request,"game.html")

def checkstatus(request):
    gameresponse={}
    gameresponse['message']="dude itsss done";
    # return HttpResponse(json.dumps(gameresponse),content_type="application/json")
    s=request.POST.get('gamestatus')
    return HttpResponse(s)