from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse


from .forms import (
    CadastrarPessoaFisicaForm, 
    CadastrarPessoaJuridicaForm,
    CadastrarEquipamentoForm,
    CadastrarItemForm,
    CadastrarOrdemServicoForm,
)

from .models import (
    PessoaJuridica,
    PessoaFisica,
    Equipamento,
    Item,
    OrdemServico
)

def index(request):
    return render(request, 'core/index.html')

def areaDoLeo(request):
    return render(request, 'core/area_do_leo.html')

def cadastrarPessoaFisica(request):
    form = CadastrarPessoaFisicaForm(request.POST or None, 
        request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'core/cadastrar_pessoa_fisica.html', {'form':form})

def cadastrarPessoaJuridica(request):
    form = CadastrarPessoaJuridicaForm(request.POST or None, 
        request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'core/cadastrar_pessoa_juridica.html', {'form':form})

def cadastrarEquipamento(request):
    equipamentos = Equipamento.objects.all()

    form = CadastrarEquipamentoForm(request.POST or None, 
        request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'core/cadastrar_equipamento.html', 
        {'form':form, 'equipamentos':equipamentos})

def cadastrarItem(request):
    form = CadastrarItemForm(request.POST or None, 
        request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'core/cadastrar_item.html', {'form':form})

def cadastrarOrdemServico(request):
    form = CadastrarOrdemServicoForm(request.POST or None, 
        request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            data = form.clean()
            for equipamento in data['equipamento']:
                equipamento.status = 'OC'
                equipamento.save()
            form.save()
            return HttpResponseRedirect(request.path_info)

    return render(request, 'core/cadastrar_ordem_servico.html', {'form':form})

def consultarClientes(request):
    clientes_pessoa_fisica = PessoaFisica.objects.all()
    clientes_pessoa_juridica = PessoaJuridica.objects.all()

    context = {
        'clientes_pessoa_fisica':clientes_pessoa_fisica,
        'clientes_pessoa_juridica':clientes_pessoa_juridica,
    }

    return render(request, 'core/consultar_clientes.html', context)