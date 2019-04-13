from django.urls import path, include
from . import views

urlpatterns = [
    path("registrar/", views.registerPage, name="register")
]