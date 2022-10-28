from token import RIGHTSHIFTEQUAL
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account ' + username + ' created successfully')
            return redirect('login:login')

    context = {'form':form}
    return render(request, 'login/register.html', context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login:login')


def profilePage(request):
    context = {}
    return render(request, 'login/profile.html', context)
