from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    path("registrar/", views.register, name="registrar"),
    path("registrar1/", views.register1, name="registrar1"),
    path("login/", views.login, name="login"),
     path("login1/", views.login1, name="login1"),
    path("logout/", views.logout_view, name="logout"),
]