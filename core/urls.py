from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('area-do-leo/', views.areaDoLeo, name='areaDoLeo'),
    path('cadastrar-pessoa-fisica/', views.cadastrarPessoaFisica, 
        name='cadastrarPessoaFisica'),
    path('cadastrar-pessoa-juridica/', views.cadastrarPessoaJuridica, 
        name='cadastrarPessoaJuridica'),
    path('cadastrar-equipamento/', views.cadastrarEquipamento, 
        name='cadastrarEquipamento'),
    path('cadastrar-item/', views.cadastrarItem, 
        name='cadastrarItem'),
    path('cadastrar-ordem-servico/', views.cadastrarOrdemServico, 
        name='cadastrarOrdemServico'),
    path('consultar-clientes/', views.consultarClientes, 
        name='consultarClientes'),
]