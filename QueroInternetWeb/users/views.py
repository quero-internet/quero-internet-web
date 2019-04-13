from django.shortcuts import render, redirect, render_to_response
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if(request.method == 'GET'):
        form = forms.RegistrationForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    else:
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
        else:
            return render_to_response('register.html', {'form':form})

def login(request):
    if(request.method == 'GET'):
        form = AuthenticationForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    else:        
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            loginUser(request, user)
            return redirect("/main")            
        else:            
            return User.DoesNotExis