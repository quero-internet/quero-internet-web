from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Parceiro(models.Model):
    razao_social = models.CharField(maxlength=80)
    nome_fantasia = models.CharField(maxlength=80)
    cnpj = models.CharField(maxlength=14)
    inscricao_estadual = models.CharField(maxlength=14)
    contato = models.CharField(maxlength=60)
    usuario_id = models.ForeignKey(User, on_delete=models.PROTECT)

class TipoAcesso(models.Model):
    nome = models.CharField(maxlength=60)

class PlanoInternet(models.Model):
    nome = models.CharField(maxlength=60)

class VelocidadeInternet(models.Model):
    nome = models.CharField(maxlength=60)

class Solicitacao(models.Model):
    tipo_acesso_id = models.ForeignKey(TipoAcesso, on_delete=models.PROTECT)
