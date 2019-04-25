from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Solicitacao, Parceiro
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        paginator = Paginator(Solicitacao.objects.filter(usuario__pk = self.request.user.pk), 10)
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
class Parceiros(TemplateView):
    template_name = 'main/parceiros.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Parceiros, self).get_context_data(*args, **kwargs)
        paginator = Paginator(Parceiro.objects.filter(usuario__pk = self.request.user.pk), 10)
        page = self.request.GET.get('page')
        parceiros = paginator.get_page(page)

        num_pages = []

        for item in range(parceiros.paginator.num_pages):
            num_pages.append(item + 1)

        context['parceiros'] = parceiros
        context['num_pages'] = num_pages
        context['username'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class SolicitacaoForm(CreateView):
    template_name = 'main/solicitacao-form.html'
    model = Solicitacao
    fields = ['tipo_acesso', 'planos_internet', 'velocidades_internet',
              'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'uf', 'cidade', 'observacoes']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return redirect("/")
    
    def get_context_data(self, **kwargs):
        context = super(SolicitacaoForm, self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context