from django.shortcuts import render
from . import forms

# Create your views here.
def registerPage(request):
    form = forms.RegistrationForm(request.POST)
    context = {'form': form}
    return render(request, 'register.html', context)