from django.shortcuts import render, redirect, render_to_response
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.conf import settings

# Create your views here.
def register(request):
    if(request.method == 'GET'):
        form = forms.RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register.html', context)
    else:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            return render_to_response('accounts/register.html', {'form':form})
def register1(request):
    if(request.method == 'GET'):
        form = forms.RegistrationForm()
        context = {'form': form}
        return render(request, 'accounts/register1.html', context)
    else:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login1')
        else:
            return render_to_response('accounts/register1.html', {'form':form})
def login(request):
    if(request.method == 'GET'):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:        
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginUser(request, user)
            return redirect("/")            
        else:            
            messages.error(request,'Usuário ou senha incorretos!')
            return redirect('accounts:login')
            
def login1(request):
    if(request.method == 'GET'):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login1.html', context)
    else:        
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginUser(request, user)
            return redirect("/")            
        else:            
            messages.error(request,'Usuário ou senha incorretos!')
            return redirect('accounts:login')
        
def logout_view(request):
    logout(request)
    return redirect(settings.LOGIN_URL)