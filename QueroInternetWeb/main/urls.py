from django.urls import path
from main import views

app_name = "main"
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('solicitacao/detalhes/<int:pk>', views.SolicitacaoDetalhe.as_view(), name='solicitacao-detalhes'),
    path('solicitacao/<int:pk>/criar-resposta', views.SolicitacaoCriarResposta.as_view(), name='solicitacao-criar-resposta'),
    path('solicitacao/editar-resposta/<int:pk>', views.SolicitacaoEditarResposta.as_view(), name='solicitacao-editar-resposta'),
    path('solicitacao/excluir-resposta/<int:pk>', views.SolicitacaoDeletarResposta.as_view(), name='solicitacao-excluir-resposta'),
    path('parceiros/', views.Parceiros.as_view(), name='parceiros'),
    path('solicitacao/novo/', views.SolicitacaoForm.as_view(), name='solicitacao-novo')
]