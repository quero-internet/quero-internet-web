from django.contrib import admin
from .models import Parceiro, PlanoInternet, TipoAcesso, VelocidadeInternet, Solicitacao

# Register your models here.
admin.site.register(Parceiro)
admin.site.register(PlanoInternet)
admin.site.register(TipoAcesso)
admin.site.register(VelocidadeInternet)
admin.site.register(Solicitacao)