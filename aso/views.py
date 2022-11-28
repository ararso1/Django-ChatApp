from datetime import date, datetime, timedelta
from multiprocessing import context
from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.


def loginpage(request):
    if request.method =="POST":
        
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            print('hellooooooooooo')
            return redirect('chat')
        else:
            messages.info(request, "Username or Password is incorrect")
    context = {}
    return render(request, 'aso/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()
    context = {'form':form}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        #customerform=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'aso/register.html', context)

@login_required(login_url='')
def update_profile(request):
    profile = request.user
    form = UpdateForm()
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            x=form.save()
            x.user = request.user
            x.save()
            return redirect('profile')
    context = {'profile':profile}

    return render(request, 'aso/update_profile.html', context)

def chat(request):
    return render(request, 'aso/chat.html')

def post(request):

    return render(request, 'aso/post.html')
    
@login_required(login_url='')
def myaccount(request):
    users = request.user
    form =  PostForm()
    if request.method == "POST":
        form = PostForm(request, request.FILES)
        print(users)
        if form.is_valid():
            print(users,'thern')
            x=form.save()
            x.user = request.user
            x.save()
            return redirect('post')
    context = {'users':users}
    return render(request, 'aso/myaccount.html', context)
