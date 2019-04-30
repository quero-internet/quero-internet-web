from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path("registrar/", views.register, name="registrar"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_view, name="logout"),
]