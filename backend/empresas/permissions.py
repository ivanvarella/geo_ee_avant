from rest_framework.permissions import BasePermission, SAFE_METHODS
from empresas.models import Empresa


# Custom permissions class
class EmpresaPermission(BasePermission):
    def has_permission(self, request, view):
        # Todos podem listar as empresas
        if request.method in SAFE_METHODS and view.action == "list":
            return True

        # Somente um responsável de empresa pode cadastrar uma empresa, caso já não tenha uma empresa vinculada
        if request.method == "POST" and view.action == "create":
            return (
                request.user.tipo == "responsavel"
                and not Empresa.objects.filter(responsavel=request.user).exists()
            )

        # Permite acesso ao endpoint apenas para usuários autenticados: outros metodos
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Verifica se é um método de leitura seguro (GET, HEAD, OPTIONS) e se a ação é listar
        if request.method in SAFE_METHODS and view.action == "list":
            return True

        # Para métodos de modificação (POST, PUT, PATCH, DELETE)
        # Somente o próprio usuário pode alterar seus dados
        return obj.responsavel == request.user
