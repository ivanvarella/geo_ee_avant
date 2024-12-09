# Django DRF
from rest_framework import viewsets

# Django RQL
from dj_rql.drf import RQLFilterBackend
from empresas.filters import EmpresaFilterClass

from empresas.models import Empresa

# Serializers
from empresas.serializers import EmpresaModelSerializer

# Para permissões personalizadas
from empresas.permissions import EmpresaPermission


class EmpresaModelViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaModelSerializer

    # Config RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = EmpresaFilterClass

    # Permissions:
    permission_classes = [EmpresaPermission]
