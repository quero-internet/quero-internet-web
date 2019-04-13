from django.urls import path, include
from . import views

urlpatterns = [
    path("registrar/", views.register, name="register"),
    path("login/", views.login, name="login"),
]