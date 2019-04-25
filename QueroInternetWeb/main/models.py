from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.


class Parceiro(models.Model):
    class Meta:
        verbose_name = "Parceiro"
        verbose_name_plural = "Parceiros"
    razao_social = models.CharField(max_length=80, verbose_name="Razão social")
    nome_fantasia = models.CharField(max_length=80)
    cnpj = models.CharField(max_length=14, verbose_name="CNPJ")
    inscricao_estadual = models.CharField(max_length=14, verbose_name="Inscrição estadual")
    contato = models.CharField(max_length=60)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.razao_social


class TipoAcesso(models.Model):
    class Meta:
        verbose_name = "Tipo de acesso"
        verbose_name_plural = "Tipos de acesso"
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class PlanoInternet(models.Model):
    class Meta:
        verbose_name = "Plano de Internet"
        verbose_name_plural = "Plano de Internet"
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class VelocidadeInternet(models.Model):
    class Meta:
        verbose_name = "Velocidade de Internet"
        verbose_name_plural = "Velocidades de Internet"
    nome = models.CharField(max_length=60)

    def __str__(self):
        return self.nome


class Solicitacao(models.Model):
    class Meta:
        verbose_name = "Solicitação"
        verbose_name_plural = "Solicitações"

    tipo_acesso = models.ForeignKey(TipoAcesso, on_delete=models.PROTECT, verbose_name="Tipo de acesso")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    logradouro = models.CharField(max_length=60)
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=60, null=True, blank=True)
    bairro = models.CharField(max_length=60)
    cidade = models.CharField(max_length=60)
    uf = models.CharField(max_length=2, verbose_name="UF")
    planos_internet = models.ManyToManyField(PlanoInternet, verbose_name="Planos de internet")
    velocidades_internet = models.ManyToManyField(VelocidadeInternet, verbose_name="Velocidades de internet")
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_e_hora = models.DateTimeField(auto_now_add=True)
    observacoes = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return "Solicitação "+ str(self.pk)
