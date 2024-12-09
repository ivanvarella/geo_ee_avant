from django.contrib import admin
from .models import (
    DadosCandidato,
    Habilidade,
    ExperienciaAcademica,
    ExperienciaProfissional,
    Idioma,
    Conquista,
    Curriculo,
)


@admin.register(DadosCandidato)
class DadosCandidatoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "genero", "deficiencia", "linkedin", "github")
    search_fields = ("usuario__username", "usuario__email", "genero")
    list_filter = ("genero", "deficiencia")
    ordering = ("usuario__username",)
    fieldsets = (
        (None, {"fields": ("usuario", "genero", "deficiencia", "tipo_deficiencia")}),
        ("Redes Sociais", {"fields": ("linkedin", "github")}),
    )


@admin.register(Habilidade)
class HabilidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "usuario")
    search_fields = ("nome", "usuario__username", "usuario__email")
    list_filter = ("usuario__username",)
    ordering = ("nome",)


@admin.register(ExperienciaAcademica)
class ExperienciaAcademicaAdmin(admin.ModelAdmin):
    list_display = ("formacao", "curso", "status", "usuario", "inicio", "fim")
    search_fields = ("formacao", "curso", "usuario__username", "instituicao")
    list_filter = ("status", "instituicao", "inicio", "fim")
    ordering = ("inicio",)


@admin.register(ExperienciaProfissional)
class ExperienciaProfissionalAdmin(admin.ModelAdmin):
    list_display = ("cargo", "empresa", "usuario", "atual", "inicio", "fim")
    search_fields = ("cargo", "empresa", "usuario__username")
    list_filter = ("empresa", "atual", "inicio", "fim")
    ordering = ("inicio",)


@admin.register(Idioma)
class IdiomaAdmin(admin.ModelAdmin):
    list_display = ("idioma", "nivel", "usuario")
    search_fields = ("idioma", "nivel", "usuario__username")
    list_filter = ("nivel",)
    ordering = ("idioma",)


@admin.register(Conquista)
class ConquistaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "usuario")
    search_fields = ("titulo", "usuario__username")
    list_filter = ("usuario__username",)
    ordering = ("titulo",)


@admin.register(Curriculo)
class CurriculoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "data_envio")
    search_fields = ("usuario__username", "usuario__email")
    list_filter = ("data_envio",)
    ordering = ("-data_envio",)
