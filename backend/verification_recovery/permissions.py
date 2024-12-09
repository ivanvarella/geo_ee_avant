from rest_framework.permissions import BasePermission, SAFE_METHODS


class AllowAny(BasePermission):
    """
    Permite acesso a qualquer usuário (autenticado ou não)
    para endpoints de recuperação de senha.
    """

    def has_permission(self, request, view):
        # Permite acesso a todos, pois é uma rota de recuperação de senha
        return True
