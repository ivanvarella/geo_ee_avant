from django.contrib import admin
from .models import Vaga, Candidatura


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "modalidade",
        "status",
        "data_publicacao",
        "data_encerramento",
    )
    search_fields = ("nome", "empresa__nome")
    list_filter = ("modalidade", "status", "pcd")


@admin.register(Candidatura)
class CandidaturaAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "usuario",
        "vaga",
        "data_candidatura",
        "status",
    )
    list_filter = ("status", "data_candidatura")
    search_fields = ("usuario__username", "vaga__nome")
    list_select_related = ("usuario", "vaga")

    def vaga_nome(self, obj):
        return obj.vaga.nome

    vaga_nome.short_description = "Vaga"

    def usuario_nome(self, obj):
        return obj.usuario.username

    usuario_nome.short_description = "Usuário"
