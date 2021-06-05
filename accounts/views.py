import re
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from . forms import CreateUserForm

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return  redirect('home')
        else:
            messages.info(request,'Username OR Password is incorrect')
            return render(request,'accounts/login.html')

    return render(request,'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was successfully created for '+ user)
            return redirect('login')

    return render(request,'accounts/register.html',{'form':form})

