from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Método para exibir o nome completo
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name.short_description = "Nome Completo"

    # Exibir os campos desejados na lista de usuários, incluindo o campo is_email_verified
    list_display = (
        "email",
        "full_name",
        "cpf",
        "username",
        "data_nascimento",
        "tipo",
        "is_email_verified",  # Adicionando o campo is_email_verified
        "is_superuser",
        "is_staff",
        "is_active",
    )
    search_fields = (
        "username",
        "email",
        "cpf",
        "first_name",
        "last_name",
        "tipo",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "data_nascimento",
        "tipo",
        "is_email_verified",  # Adicionando filtro para is_email_verified
    )

    # Definir quais campos serão exibidos no formulário de detalhes do usuário
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Informações pessoais"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "cpf",
                    "data_nascimento",
                    "email",
                    "tipo",
                    "is_email_verified",  # Adicionando is_email_verified no formulário
                )
            },
        ),
        (
            _("Permissões"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Datas importantes"), {"fields": ("last_login", "date_joined")}),
    )

    # Definir quais campos estarão disponíveis ao criar um novo usuário
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "cpf",
                    "data_nascimento",
                    "password1",
                    "password2",
                    "email",
                    "tipo",
                    "is_email_verified",  # Adicionando is_email_verified ao criar
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    # Campos para ordenação dos objetos no admin
    ordering = ("username",)


# Registro do CustomUser no admin
admin.site.register(CustomUser, CustomUserAdmin)
