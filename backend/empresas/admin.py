from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_empresa",
        "responsavel",
        "email_corporativo",
        "cnpj",
        "numero_funcionarios",
        "segmento_empresa",
    )
    search_fields = (
        "nome_empresa",
        "email_corporativo",
        "cnpj",
        "responsavel__username",
    )
    list_filter = ("segmento_empresa", "responsavel")
    ordering = ("nome_empresa",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "responsavel",
                    "nome_empresa",
                    "cnpj",
                    "email_corporativo",
                    "segmento_empresa",
                )
            },
        ),
        (
            "Redes Sociais",
            {"fields": ("site_empresa", "linkedin_empresa", "instagram_empresa")},
        ),
        (
            "Informações Adicionais",
            {
                "fields": (
                    "numero_funcionarios",
                    "informacoes_empresa",
                    "logo",
                    "banner",
                    "endereco",
                )
            },
        ),
    )
