# Django DRF
from rest_framework import viewsets

# Django RQL
from dj_rql.drf import RQLFilterBackend
from shareds.filters import (
    EnderecoFilterClass,
    TelefoneFilterClass,
    CepSourceApiFilterClass,
)

from shareds.models import Endereco, Telefone, CepSourceApi


# Serializers
from shareds.serializers import (
    EnderecoModelSerializer,
    TelefoneModelSerializer,
    CepSourceApiModelSerializer,
)

# Para permissões personalizadas
from shareds.permissions import (
    EnderecoPermission,
    TelefonePermission,
    CepSourceApiPermission,
)


class EnderecoModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:  # Verifica se o usuário está autenticado
            if user.tipo in ["administrador", "funcionario"]:
                return Endereco.objects.all()  # Todos os endereços
            return Endereco.objects.filter(usuario=user)  # Apenas endereços do usuário
        return Endereco.objects.none()  # Retorna queryset vazio se não autenticado

    serializer_class = EnderecoModelSerializer

    # Config RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = EnderecoFilterClass

    # Permissions:
    permission_classes = [EnderecoPermission]


class TelefoneModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:  # Verifica se o usuário está autenticado
            if user.tipo in ["administrador", "funcionario"]:
                return Telefone.objects.all()  # Todos os endereços
            return Telefone.objects.filter(usuario=user)  # Apenas endereços do usuário
        return Telefone.objects.none()  # Retorna queryset vazio se não autenticado

    serializer_class = TelefoneModelSerializer

    # Config RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = TelefoneFilterClass

    # Permissions:
    permission_classes = [TelefonePermission]


class CepSourceApiModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:  # Verifica se o usuário está autenticado
            if user.tipo in ["administrador", "funcionario"]:
                return CepSourceApi.objects.all()  # Todos os endereços
            return CepSourceApi.objects.none()  # Vazio se não for admin ou funcionário
        return CepSourceApi.objects.none()  # Retorna queryset vazio se não autenticado

    serializer_class = CepSourceApiModelSerializer

    # Config RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CepSourceApiFilterClass

    # Permissions:
    permission_classes = [CepSourceApiPermission]
