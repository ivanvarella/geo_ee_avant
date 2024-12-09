from rest_framework.permissions import BasePermission, SAFE_METHODS


# TODO: Verificar permissions de Candidato
# Custom permissions class
class CandidatoCustomUserPermission(BasePermission):
    # Permissão ao Endpoint
    def has_permission(self, request, view):
        # Permite criação para todos
        if request.method == "POST" and view.action == "create":
            return True

        # Para listagem, requer autenticação
        if request.method in SAFE_METHODS and view.action == "list":
            return request.user.is_authenticated

        # Para outros métodos (PATCH, PUT, DELETE), autenticação é necessária
        return request.user.is_authenticated

    # Permissão de objeto
    def has_object_permission(self, request, view, obj):
        # Só permite acessar e editar (incluindo o delete) os próprios dados
        return obj == request.user


# TODO: Verificar permissions de Funcionario
class FuncionarioCustomUserPermission(BasePermission):
    # Permissão ao Endpoint
    def has_permission(self, request, view):
        return request.user.tipo == "funcionario"

    # Permissão de objeto
    def has_object_permission(self, request, view, obj):
        # Mesmo sendo staff (funcinários) acessem e modifiquem somente seus objetos
        return obj == request.user


# TODO: Verificar permissions de Responsavel
class ResponsavelCustomUserPermission(BasePermission):
    # Permissão ao Endpoint
    def has_permission(self, request, view):
        # Permite criação para todos
        if request.method == "POST" and view.action == "create":
            return True

        # Para listagem, requer autenticação
        if request.method in SAFE_METHODS and view.action == "list":
            return request.user.is_authenticated

        # Para outros métodos (PATCH, PUT, DELETE), autenticação é necessária
        return request.user.is_authenticated

    # Permissão de objeto
    def has_object_permission(self, request, view, obj):
        # Só permite acessar e editar (incluindo o delete) os próprios dados
        return obj == request.user


# TODO: Verificar permissions de Admin
class AdminCustomUserPermission(BasePermission):
    # Permissão ao Endpoint
    def has_permission(self, request, view):
        return request.user.tipo == "administrador"

    # Permissão de objeto
    def has_object_permission(self, request, view, obj):
        # Permite que superusuários acessem e modifiquem qualquer objeto
        return request.user.tipo == "administrador"
