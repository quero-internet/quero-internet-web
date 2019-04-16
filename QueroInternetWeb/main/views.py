from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Solicitacao
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    solicitacao_list = Solicitacao.objects.all()
    paginator = Paginator(solicitacao_list, 10)
    page = request.GET.get('page')
    solicitacoes = paginator.get_page(page)
    return render(request, 'index.html', {'solicitacoes': solicitacoes, 'username': request.user})
