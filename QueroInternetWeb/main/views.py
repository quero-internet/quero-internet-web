from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Solicitacao
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        paginator = Paginator(Solicitacao.objects.all(), 10)
        page = self.request.GET.get('page')
        solicitacoes = paginator.get_page(page)

        num_pages = []

        for item in range(solicitacoes.paginator.num_pages):
            num_pages.append(item + 1)

        context['solicitacoes'] = solicitacoes
        context['num_pages'] = num_pages
        context['username'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class SolicitacaoForm(CreateView):
    template_name = 'main/solicitacao-form.html'
    model = Solicitacao
    fields = ['tipo_acesso', 'planos_internet', 'velocidades_internet',
              'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'uf', 'cidade']