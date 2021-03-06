from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    is_staff = forms.BooleanField(label="Desejo ser um parceiro.", required=False)
    username = forms.CharField(label = "Nome de usuario")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Senha (Repita a senha)")


    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2', 'is_staff' )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.is_staff

        if commit:
            user.save()

        return user

        
