from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from main.models import Parceiro, Solicitacao
from datetime import date
import json
from django.db.models import Sum, Count
from django.core import serializers

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
        context['quantitativo_por_situacao_data'] = self.get_quantitativo_por_situacao_data()
        context['quantitativo_respondido_data'] = self.get_quantitativo_respondido_data()
        context['quantitativo_conversoes_por_data'] = self.get_quantitativo_conversoes_por_data()
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

    def get_quantitativo_por_situacao_data(self):
        fechadas = Solicitacao.objects.filter(parceiro_escolhido__isnull = False).count()
        abertas = Solicitacao.objects.filter(parceiro_escolhido__isnull = True).count()
        
        return json.dumps([abertas, fechadas])

    def get_quantitativo_respondido_data(self):
        respondido = Solicitacao.objects.filter(respostas__isnull = False).count()
        respondido_convertido = Solicitacao.objects.filter(respostas__isnull = False, parceiro_escolhido__pk=self.request.user.parceiro.pk).count()
        nao_respondido = Solicitacao.objects.filter(respostas__isnull = True).count()
        
        return json.dumps([nao_respondido, respondido, respondido_convertido])

    def get_quantitativo_conversoes_por_data(self):
        qs = Solicitacao.objects.filter(parceiro_escolhido__pk=self.request.user.parceiro.pk)
        qs = qs.extra(select={'data_e_hora':'DATE(data_e_hora)'})
        qs = qs.values('data_e_hora').annotate(Count('pk'))
        return json.dumps(list(qs))