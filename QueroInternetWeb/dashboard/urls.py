from django.urls import path
from main import views

app_name = "dashboard"
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    ]