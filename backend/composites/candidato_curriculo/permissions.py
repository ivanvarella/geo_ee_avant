from rest_framework.permissions import BasePermission, SAFE_METHODS

from candidatos.models import (
    Habilidade,
    ExperienciaAcademica,
    ExperienciaProfissional,
    Idioma,
    Conquista,
    Curriculo,
)


class ExperienciaAcademicaPermission(BasePermission):
    """
    Permissões customizadas para o endpoint CandidatoCurriculo:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class ExperienciaProfissionalPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class IdiomaPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class HabilidadePermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class ConquistaPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class CurriculoPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS:
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class CandidatoCurriculoPermissions(BasePermission):
    """
    Combina as permissões acima.
    """

    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            return False

        # Aplica permissões dos modelos individuais
        return (
            ExperienciaAcademicaPermission().has_permission(request, view)
            and ExperienciaProfissionalPermission().has_permission(request, view)
            and IdiomaPermission().has_permission(request, view)
            and HabilidadePermission().has_permission(request, view)
            and ConquistaPermission().has_permission(request, view)
            and CurriculoPermission().has_permission(request, view)
        )

    def has_object_permission(self, request, view, obj):
        # Aplica permissões de objetos específicos para cada modelo
        if isinstance(obj, ExperienciaAcademica):
            return ExperienciaAcademicaPermission().has_object_permission(
                request, view, obj
            )
        elif isinstance(obj, ExperienciaProfissional):
            return ExperienciaProfissionalPermission().has_object_permission(
                request, view, obj
            )
        elif isinstance(obj, Idioma):
            return IdiomaPermission().has_object_permission(request, view, obj)
        elif isinstance(obj, Habilidade):
            return HabilidadePermission().has_object_permission(request, view, obj)
        elif isinstance(obj, Conquista):
            return ConquistaPermission().has_object_permission(request, view, obj)
        elif isinstance(obj, Curriculo):
            return CurriculoPermission().has_object_permission(request, view, obj)
        return False
