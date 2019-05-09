from django.views.generic.list import ListView
from .models import Solicitacao, Parceiro, Resposta
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect,get_object_or_404,render
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from django.core.exceptions import PermissionDenied
from django.urls import reverse

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        user = self.request.user

        solicitacoes_paginadas = []

        if(user.is_staff):
            solicitacoes_paginadas = Solicitacao.objects.all()
        else:
            solicitacoes_paginadas = Solicitacao.objects.filter(usuario__pk = self.request.user.pk)
        

        paginator = Paginator(solicitacoes_paginadas, 10)
        page = self.request.GET.get('page')
        solicitacoes = paginator.get_page(page)

        num_pages = []

        for item in range(solicitacoes.paginator.num_pages):
            num_pages.append(item + 1)

        context['solicitacoes'] = solicitacoes
        context['num_pages'] = num_pages
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
        return redirect("main:home")

@method_decorator(login_required, name='dispatch')
class SolicitacaoDetalhe(DetailView):
    template_name = 'main/solicitacao-detalhe.html'
    model = Solicitacao

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class SolicitacaoCriarResposta(CreateView):
    template_name = 'main/solicitacao-criar-resposta.html'
    model = Resposta
    fields = ['resposta', 'valor_implantacao', 'valor_mensalidade']
    widgets = {
        'resposta': forms.CharField(widget=forms.Textarea)
    }

    def form_valid(self, form):
        self.object = form.save(commit=False)
        id_solicitacao = self.kwargs['pk']
        self.object.solicitacao = get_object_or_404(Solicitacao, pk=id_solicitacao)
        self.object.usuario = self.request.user

        if self.object.usuario.parceiro is None:
            raise PermissionDenied("Seu usuário precisa ter uma empresa vinculada a ele para responder!")

        self.object.save()
        return redirect('main:solicitacao-detalhes', pk=self.object.solicitacao.pk)

@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class SolicitacaoEditarResposta(UpdateView):
    template_name = 'main/solicitacao-editar-resposta.html'
    model = Resposta
    fields = ['resposta', 'valor_implantacao', 'valor_mensalidade']
    widgets = {
        'resposta': forms.CharField(widget=forms.Textarea)
    }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if(self.object.usuario.pk != self.request.user.pk):
            raise PermissionDenied("Você não tem permissão para editar esse registro!")

        return ctx

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user

        if self.object.usuario.parceiro is None:
            raise PermissionDenied("Seu usuário precisa ter uma empresa vinculada a ele para responder!")

        self.object.save()
        return redirect('main:solicitacao-detalhes', pk=self.object.solicitacao.pk)
        
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class SolicitacaoDeletarResposta(DeleteView):
    model = Resposta
    template_name = 'main/solicitacao-remover-resposta.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if(self.object.usuario.pk != self.request.user.pk):
            raise PermissionDenied("Você não tem permissão para editar esse registro!")

        return ctx

    def get_success_url(self):
        return reverse('main:solicitacao-detalhes', kwargs={'pk':self.object.solicitacao.pk})


    