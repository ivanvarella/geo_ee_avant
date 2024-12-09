from rest_framework.permissions import BasePermission, SAFE_METHODS


# Custom permissions class
class VagaPermission(BasePermission):
    def has_permission(self, request, view):
        # Para listagem: todos podem
        if request.method in SAFE_METHODS and view.action == "list":
            return True

        # Somente um responsável de empresa pode cadastrar uma vaga
        if request.method == "POST" and view.action == "create":
            return request.user.tipo == "responsavel"

        # Para outros métodos: autenticação
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Verifica se é um método de leitura seguro (GET, HEAD, OPTIONS)
        # e se a ação é listar
        if request.method in SAFE_METHODS and view.action == "list":
            return True

        # Para criação, edição ou exclusão (POST, PUT, PATCH, DELETE):
        # Somente o responsável pela empresa associada à vaga pode
        # modificar ou deletar
        return obj.empresa.responsavel == request.user


class CandidaturaPermission(BasePermission):
    def has_permission(self, request, view):
        # Somente um candidato pode se candidatar à uma vaga
        if request.method == "POST" and view.action == "create":
            return request.user.tipo == "candidato"

        # Não pode deletar, só será deletado quando a vaga que
        # está atralado a candidatura for deletada
        if request.method == "DELETE":
            return False

        # Outros métodos: autenticado
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated
