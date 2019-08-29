from django.contrib import admin
from .models import Parceiro, PlanoInternet, TipoAcesso, VelocidadeInternet, Solicitacao

admin.site.site_header = "Quero Internet!"
admin.site.site_title = "Quero Internet!"

# Register your models here.
admin.site.register(Parceiro)
admin.site.register(PlanoInternet)
admin.site.register(TipoAcesso)
admin.site.register(VelocidadeInternet)

# Personalizando form de solicitação
@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'usuario', 'tipo_acesso', 'cidade', 'uf']
    list_filter = ['cidade', 'uf', 'tipo_acesso',
                   'planos_internet', 'velocidades_internet']
    fieldsets = [
        ('Etapa 1', {
            'fields': ['tipo_acesso', 'planos_internet']
        }),
        ('Etapa 2', {
            'fields': ['velocidades_internet']
        }),
        ('Etapa 3', {
            'fields': ['cep', 'logradouro', 'numero', 'complemento', 'bairro', 'uf', 'cidade','usuario']
        }),
    ]
