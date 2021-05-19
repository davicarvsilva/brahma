from django.contrib import admin

from .models import (
    PessoaFisica,
    PessoaJuridica,
    Equipamento,
    Item,
    OrdemServico
)

admin.site.register(PessoaJuridica)
admin.site.register(PessoaFisica)
admin.site.register(Equipamento)
admin.site.register(Item)
admin.site.register(OrdemServico)
