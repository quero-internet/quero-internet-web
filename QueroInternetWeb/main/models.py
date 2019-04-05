from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Parceiro(models.Model):
    razao_social = models.CharField(max_length=80)
    nome_fantasia = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=14)
    inscricao_estadual = models.CharField(max_length=14)
    contato = models.CharField(max_length=60)
    usuario_id = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.razao_social


class TipoAcesso(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class PlanoInternet(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class VelocidadeInternet(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    tipo_acesso_id = models.ForeignKey(TipoAcesso, on_delete=models.PROTECT)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=60)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2)
    planos_internet = models.ManyToManyField(PlanoInternet)
    velocidades_internet = models.ManyToManyField(VelocidadeInternet)
    usuario_id = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "Solicitação "+self.pk
