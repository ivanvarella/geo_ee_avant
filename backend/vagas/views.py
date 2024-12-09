# Django DRF
from rest_framework import viewsets

# Django RQL
from dj_rql.drf import RQLFilterBackend
from vagas.filters import VagaFilterClass, CandidaturaFilterClass

from vagas.models import Vaga, Candidatura

# Serializers
from vagas.serializers import VagaModelSerializer, CandidaturaModelSerializer

# Para permissões personalizadas
from vagas.permissions import VagaPermission, CandidaturaPermission


class VagaModelViewSet(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()  # As vagas serão vistas por todos sempre
    serializer_class = VagaModelSerializer

    # Config RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = VagaFilterClass

    # Permissions:
    permission_classes = [VagaPermission]


class CandidaturaModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        user = self.request.user

        # Para listagem (GET em /candidaturas/), aplica os filtros
        if self.action == "list":
            if user.tipo == "candidato":
                return Candidatura.objects.filter(usuario=user)
            elif user.tipo == "responsavel":
                return Candidatura.objects.filter(vaga__empresa__responsavel=user)
            return Candidatura.objects.all()

        # Para outras ações (retrieve, update, etc), retorna todos os objetos
        # e deixa as permissões controlarem o acesso
        return Candidatura.objects.all()

    serializer_class = CandidaturaModelSerializer

    # Config RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CandidaturaFilterClass

    # Permissions:
    permission_classes = [CandidaturaPermission]
