from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('parceiros/', views.Parceiros.as_view(), name='parceiros'),
    path('novo/', views.SolicitacaoForm.as_view(), name='novo')
]