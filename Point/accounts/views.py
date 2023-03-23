from http.client import HTTPResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from portfolio.models import Student
from django.shortcuts import render, redirect
from edumarket.models import Educator

def index(request):
    return render(request, "accounts/index.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        created_user = User.objects.create_user(username, email, password)
        created_user.save()
        
        student = Student(user = created_user)
        student.save()

        return redirect('signin')
    return render(request, "accounts/register.html")

def signin(request):
    if request.method == "POST":
        us = request.POST['username']
        pd = request.POST['password']

        user = authenticate(username = us, password = pd)

        if user is not None:
            login(request, user)
            return redirect("/portfolio")
        else:
            return redirect("/accounts")

    return render(request, "accounts/signin.html")

def signout(request):
    logout(request)
    return redirect("/accounts")
