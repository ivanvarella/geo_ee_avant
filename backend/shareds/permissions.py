from rest_framework.permissions import BasePermission, SAFE_METHODS


# Custom permissions class
class EnderecoPermission(BasePermission):
    def has_permission(self, request, view):
        # Permite acesso ao endpoint apenas para usuários autenticados
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Verifica se é um método de leitura seguro (GET, HEAD, OPTIONS) e se a ação é listar
        if request.method in SAFE_METHODS and view.action == "list":
            if request.user.tipo in ["administrador", "funcionario"]:
                # Admins e funcionários podem listar todos os endereços -> Se autenticados
                return True
            elif request.user.tipo in ["responsavel", "candidato"]:
                # Outros usuários só podem listar seus próprios endereços
                return obj.user == request.user

        # Para métodos de modificação (POST, PUT, PATCH, DELETE)
        # Somente o próprio usuário pode alterar seus dados
        return obj.user == request.user


class TelefonePermission(BasePermission):
    def has_permission(self, request, view):
        # Permite acesso ao endpoint apenas para usuários autenticados
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Verifica se é um método de leitura seguro (GET, HEAD, OPTIONS) e se a ação é listar
        if request.method in SAFE_METHODS and view.action == "list":
            if request.user.tipo in ["administrador", "funcionario"]:
                # Admins e funcionários podem listar todos os endereços -> Se autenticados
                return True
            elif request.user.tipo in ["responsavel", "candidato"]:
                # Outros usuários só podem listar seus próprios endereços
                return obj.user == request.user

        # Para métodos de modificação (POST, PUT, PATCH, DELETE)
        # Somente o próprio usuário pode alterar seus dados
        return obj.user == request.user


class CepSourceApiPermission(BasePermission):
    # Permissão ao Endpoint
    def has_permission(self, request, view):
        # Permite acesso ao endpoint por todos autenticados -> para criação
        if request.method == "POST" and view.action == "create":
            return request.user.is_authenticated

        # Admins autenticados podem acessar os outros métodos (GET, PUT, PATCH, DELETE)
        return request.user.is_authenticated and request.user.tipo == "administrador"

    # Permissão de objeto
    def has_object_permission(self, request, view):
        # Apenas admins autenticados têm permissão de acesso ao objeto
        return request.user.is_authenticated and request.user.tipo == "administrador"
