from django.db import models

class PessoaFisica(models.Model):
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=12)
    data_instalacao = models.DateField()

    def __str__(self):
        return self.nome

class PessoaJuridica(models.Model):
    razao_social = models.CharField(max_length=100, unique=True)
    nome_fantasia = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=100, unique=True)
    celular = models.CharField(max_length=12)
    nome_contato = models.CharField(max_length=50)
    data_instalacao = models.DateField()

    def __str__(self):
        return self.nome_fantasia

class Equipamento(models.Model):
    OCUPADO = 'OC'
    DISPONIVEL = 'DI'
    DEFEITO = 'DE'

    STATUS_EQUIPAMENTOS = ( 
        (DISPONIVEL, 'Disponivel'),
        (OCUPADO, 'Ocupado'),
        (DEFEITO, 'Defeito'),
    )

    nome = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=2, choices=STATUS_EQUIPAMENTOS, default=DISPONIVEL)

    def __str__(self):
        return self.nome

class Item(models.Model):
    descricao = models.CharField(max_length=100)
    qtd_estoque = models.PositiveIntegerField()
    def __str__(self):
        return self.descricao

class OrdemServico(models.Model):
    pessoa_fisica = models.ForeignKey(PessoaFisica, 
        on_delete=models.CASCADE, null=True, blank=True)
    pessoa_juridica = models.ForeignKey(PessoaJuridica, 
        on_delete=models.CASCADE, null=True, blank=True)
    dia = models.DateField()
    descricao = models.CharField(max_length=1000, null=True, blank=True)
    equipamento = models.ManyToManyField(Equipamento)
    itens = models.ManyToManyField(Item, blank=True)
    assepsia = models.BooleanField()

    