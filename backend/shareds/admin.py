from django.contrib import admin
from .models import Endereco, Telefone, CepSourceApi


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        "usuario",
        "cep",
        "logradouro",
        "numero",
        "bairro",
        "localidade",
        "uf",
        "estado",
        "regiao",
    ]
    list_filter = ["uf", "estado"]
    search_fields = ["logradouro", "localidade", "cep", "bairro"]
    ordering = ["usuario", "localidade"]


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ["usuario", "numero", "tipo"]
    list_filter = ["tipo"]
    search_fields = ["numero"]
    ordering = ["tipo"]


@admin.register(CepSourceApi)
class CepSourceApiAdmin(admin.ModelAdmin):
    list_display = [
        "cep",
        "logradouro",
        "bairro",
        "localidade",
        "uf",
        "estado",
        "regiao",
        "ddd",
        "ibge",
        "siafi",
        "criado_em",
    ]
    list_filter = ["uf", "regiao", "estado"]
    search_fields = [
        "cep",
        "logradouro",
        "bairro",
        "localidade",
        "ibge",
        "ddd",
        "siafi",
    ]
    ordering = ["cep", "localidade"]
