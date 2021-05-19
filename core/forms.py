from django import forms

from .models import (
    PessoaFisica, 
    PessoaJuridica,
    Equipamento,
    Item,
    OrdemServico
)

class CadastrarPessoaFisicaForm(forms.ModelForm):
    class Meta:
        model = PessoaFisica

        fields = [
            'nome',
            'celular',
            'data_instalacao'
        ]

    def __init__(self, *args, **kwargs):
        super(CadastrarPessoaFisicaForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = "Nome do cliente"
        self.fields['celular'].label = "Celular do cliente"
        self.fields['data_instalacao'].label = "Data de Instalação"
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CadastrarPessoaJuridicaForm(forms.ModelForm):
    class Meta:
        model = PessoaJuridica

        fields = [
            'razao_social',
            'nome_fantasia',
            'cnpj',
            'celular',
            'nome_contato',
            'data_instalacao', 
        ]

    def __init__(self, *args, **kwargs):
        super(CadastrarPessoaJuridicaForm, self).__init__(*args, **kwargs)
        self.fields['razao_social'].label = 'Razão Social'
        self.fields['nome_fantasia'].label = 'Nome Fantasia'
        self.fields['cnpj'].label = 'CNPJ'
        self.fields['celular'].label = 'Número de Celular'
        self.fields['nome_contato'].label = 'Nome do Contato'
        self.fields['data_instalacao'].label = 'Data de Instalação'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CadastrarEquipamentoForm(forms.ModelForm):
    class Meta:
        model =  Equipamento
        fields = [
            'nome',
            'status'
        ]

    def __init__(self, *args, **kwargs):
        super(CadastrarEquipamentoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].label = 'Nome do equipamento'
        self.fields['status'].label = 'Status do Equipamento'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CadastrarItemForm(forms.ModelForm):
    class Meta:
        model =  Item
        fields = [
            'descricao',
            'qtd_estoque'
        ]

    def __init__(self, *args, **kwargs):
        super(CadastrarItemForm, self).__init__(*args, **kwargs)
        self.fields['descricao'].label = 'Nome do Item'
        self.fields['qtd_estoque'].label = 'Quantidade em estoque'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CadastrarOrdemServicoForm(forms.ModelForm):
    class Meta:
        model =  OrdemServico
        fields = [
            'pessoa_fisica',
            'pessoa_juridica',
            'dia',
            'descricao',
            'equipamento',
            'itens',
            'assepsia',
        ]

        widgets = {
			'equipamento': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(CadastrarOrdemServicoForm, self).__init__(*args, **kwargs)
        self.fields['equipamento'].queryset = Equipamento.objects.filter(
            status = 'DI')
        self.fields['descricao'].label = 'Descrição do que foi feito'
        self.fields['dia'].label = 'Dia que foi executado o serviço'
        self.fields['itens'].label = 'Itens que foram deixados'
        self.fields['assepsia'].label = 'Assepsia foi feita?'

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'