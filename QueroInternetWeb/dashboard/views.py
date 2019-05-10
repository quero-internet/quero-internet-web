from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from main.models import Parceiro, Solicitacao
from datetime import date

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Dashboard, self).get_context_data(*args, **kwargs)
        context['solicitacoesMes'] = self.get_numero_solicitacoes_mes()
        context['solicitacoesHoje'] = self.get_numero_solicitacoes_hoje()
        context['solicitacoesAno'] = self.get_numero_solicitacoes_ano()
        return context

    def get_numero_solicitacoes_mes(self):
        today = date.today()
        return Solicitacao.objects.filter(data_e_hora__month=today.month).count()
    
    def get_numero_solicitacoes_hoje(self):
        today = date.today()
        return Solicitacao.objects.filter(data_e_hora__day=today.day).count()
    
    def get_numero_solicitacoes_ano(self):
        today = date.today()
        return Solicitacao.objects.filter(data_e_hora__year=today.year).count()