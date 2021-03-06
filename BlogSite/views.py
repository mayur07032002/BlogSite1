from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
import datetime
import random


data = []
code_generated = 0



def index(request):
    return render(request, 'index.html', {'name': None})


def __login__(request):
    if request.method == 'POST':
        loginusername = request.POST.get('username')
        loginpassword = request.POST.get('password')
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Successful!!")
            return redirect('main')
        else:
            messages.warning(request,"Invalid Credentials.")
            return redirect('login')
    return render(request, 'login.html')


def signin(request):
    return render(request, 'sign.html')


def verify_code(request):
    if request.method=='POST':
        code_recieved = request.POST.get('code')
        if str(code_generated) == code_recieved:
            newuser = User.objects.create_user(data[3], data[2], data[4])
            newuser.first_name = data[0]
            newuser.last_name = data[1]
            newuser.save()
            messages.success(request,"Signed up successfully!!")
            return redirect('login')
    return redirect('login')


def sendcode(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')
    global data
    data = [fname, lname, email, user, password]
    newuser = User.objects.create_user(data[3], data[2], data[4])
    newuser.first_name = data[0]
    newuser.last_name = data[1]
    newuser.save()
    messages.success(request,"Signed up successfully!!")
    return redirect('login')

def __logout__(request):
    logout(request)
    messages.success(request,"Logout Successful!!")
    return redirect('main')

def change_user(request):
    return HttpResponse("Change username")


def change_pass(request):
    return HttpResponse("Change password")

def about(request):
    return render(request,'about.html')
