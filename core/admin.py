from django.contrib import admin

from .models import Cargo, Servico, Funcionario


@admin.register(Cargo)
class CargoAdmim(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carg', 'ativo', 'modificado')
