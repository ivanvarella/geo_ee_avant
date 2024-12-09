# Django DRF
from rest_framework import viewsets

# Django RQL
from dj_rql.drf import RQLFilterBackend
from users.filters import UserFilterClass

from users.models import CustomUser

# Serializers
from users.serializers import (
    CandidatoUserModelSerializer,
    AdminUserModelSerializer,
    FuncionarioUserModelSerializer,
    ResponsavelUserModelSerializer,
)

# Para permissões personalizadas
from users.permissions import (
    CandidatoCustomUserPermission,
    AdminCustomUserPermission,
    FuncionarioCustomUserPermission,
    ResponsavelCustomUserPermission,
)


# ViewSet
class CandidatoUserModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # Retorna apenas os dados do usuário autenticado
        if self.request.user.is_authenticated:
            return CustomUser.objects.filter(id=self.request.user.id)
        return CustomUser.objects.none()  # Nenhum dado para usuários não autenticados

    serializer_class = CandidatoUserModelSerializer

    # Configs do RQL:
    filter_backends = [RQLFilterBackend]
    rql_filter_class = UserFilterClass

    # Permissions:
    permission_classes = [CandidatoCustomUserPermission]


class FuncionarioUserModelViewSet(viewsets.ModelViewSet):
    # Tudo menos o superuser (admin)
    queryset = CustomUser.objects.exclude(is_superuser=True)
    serializer_class = FuncionarioUserModelSerializer

    # Configs do RQL:
    filter_backends = [RQLFilterBackend]
    rql_filter_class = UserFilterClass

    # Permissions:
    permission_classes = [FuncionarioCustomUserPermission]


class ResponsavelUserModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # Retorna apenas os dados do usuário autenticado
        if self.request.user.is_authenticated:
            return CustomUser.objects.filter(id=self.request.user.id)
        return CustomUser.objects.none()  # Nenhum dado para usuários não autenticados

    serializer_class = ResponsavelUserModelSerializer

    # Configs do RQL:
    filter_backends = [RQLFilterBackend]
    rql_filter_class = UserFilterClass

    # Permissions:
    permission_classes = [ResponsavelCustomUserPermission]


class AdminUserModelViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AdminUserModelSerializer

    # Configs do RQL:
    filter_backends = [RQLFilterBackend]
    rql_filter_class = UserFilterClass

    # Permissions:
    permission_classes = [AdminCustomUserPermission]
