from rest_framework.permissions import BasePermission, SAFE_METHODS

from candidatos.models import DadosCandidato
from shareds.models import Endereco, Telefone


class DadosCandidatoPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado
        if not user.is_authenticated:
            return False

        # Para métodos de leitura seguros
        if request.method in SAFE_METHODS:
            return True

        # Apenas candidatos podem criar novos dados (POST)
        if request.method == "POST":
            return user.tipo == "candidato"

        # Outros métodos de modificação são restritos para não-candidatos
        if request.method not in SAFE_METHODS:
            return user.tipo == "candidato"

        return False

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Visualização: Candidatos só podem acessar seus próprios dados
        if request.method in SAFE_METHODS:
            return obj.usuario == user

        # Modificação: Somente o próprio candidato pode alterar seus dados
        return obj.usuario == user


class EnderecoPermission(BasePermission):
    """
    Permissões para o endpoint Endereco.
    """

    def has_permission(self, request, view):
        # Apenas usuários autenticados podem acessar
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Visualização: Admins podem acessar todos os dados; outros, somente os próprios
        if request.method in SAFE_METHODS:
            if user.tipo in ["administrador", "funcionario"]:
                return True
            return obj.user == user

        # Modificação: Somente o próprio usuário pode alterar seus dados
        return obj.user == user


class TelefonePermission(BasePermission):
    """
    Permissões para o endpoint Telefone.
    """

    def has_permission(self, request, view):
        # Apenas usuários autenticados podem acessar
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Visualização: Admins podem acessar todos os dados; outros, somente os próprios
        if request.method in SAFE_METHODS:
            if user.tipo in ["administrador", "funcionario"]:
                return True
            return obj.user == user

        # Modificação: Somente o próprio usuário pode alterar seus dados
        return obj.user == user


class CandidatoDetalhesPermissions(BasePermission):
    """
    Combina as permissões para DadosCandidato, Endereco e Telefone.
    """

    def has_permission(self, request, view):
        # Verifica se o usuário está autenticado
        if not request.user.is_authenticated:
            return False

        # Aplica permissões dos modelos individuais
        return (
            DadosCandidatoPermission().has_permission(request, view)
            and EnderecoPermission().has_permission(request, view)
            and TelefonePermission().has_permission(request, view)
        )

    def has_object_permission(self, request, view, obj):
        # Aplica permissões de objetos específicos para cada modelo
        if isinstance(obj, DadosCandidato):
            return DadosCandidatoPermission().has_object_permission(request, view, obj)
        elif isinstance(obj, Endereco):
            return EnderecoPermission().has_object_permission(request, view, obj)
        elif isinstance(obj, Telefone):
            return TelefonePermission().has_object_permission(request, view, obj)
        return False
