# Django DRF
from rest_framework import viewsets

# Django RQL
from dj_rql.drf import RQLFilterBackend

# Importar as classes de filtro RQL (a serem criadas)
from candidatos.filters import (
    DadosCandidatoFilterClass,
    HabilidadeFilterClass,
    ExperienciaAcademicaFilterClass,
    ExperienciaProfissionalFilterClass,
    IdiomaFilterClass,
    ConquistaFilterClass,
    CurriculoFilterClass,
)

# Importar os modelos do app candidatos
from candidatos.models import (
    DadosCandidato,
    Habilidade,
    ExperienciaAcademica,
    ExperienciaProfissional,
    Idioma,
    Conquista,
    Curriculo,
)

# Importar os serializers (a serem criados)
from candidatos.serializers import (
    DadosCandidatoModelSerializer,
    HabilidadeModelSerializer,
    ExperienciaAcademicaModelSerializer,
    ExperienciaProfissionalModelSerializer,
    IdiomaModelSerializer,
    ConquistaModelSerializer,
    CurriculoModelSerializer,
)

# Para permissões personalizadas
from candidatos.permissions import (
    DadosCandidatoPermission,
    HabilidadePermission,
    ExperienciaAcademicaPermission,
    ExperienciaProfissionalPermission,
    IdiomaPermission,
    ConquistaPermission,
    CurriculoPermission,
)


# TODO: Documentação: Remover para o deploy
# Função para alterar a consulta do get_queryset quando user o swagger e redoc
def is_swagger_request(request):
    """Verifica se a requisição está vindo do Swagger/ReDoc"""
    return (
        hasattr(request, "accepted_renderer")
        and hasattr(request.accepted_renderer, "format")
        and request.accepted_renderer.format == "openapi"
    )


class DadosCandidatoModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return DadosCandidato.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return DadosCandidato.objects.filter(usuario=user)
        else:
            return DadosCandidato.objects.all()

    serializer_class = DadosCandidatoModelSerializer

    # Configuração do RQL
    filter_backends = [RQLFilterBackend]
    rql_filter_class = DadosCandidatoFilterClass

    # Permissions:
    permission_classes = [DadosCandidatoPermission]


class HabilidadeModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return Habilidade.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return Habilidade.objects.filter(usuario=user)
        else:
            return Habilidade.objects.all()

    serializer_class = HabilidadeModelSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = HabilidadeFilterClass

    # Permissions:
    permission_classes = [HabilidadePermission]


class ExperienciaAcademicaModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return ExperienciaAcademica.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return ExperienciaAcademica.objects.filter(usuario=user)
        else:
            return ExperienciaAcademica.objects.all()

    serializer_class = ExperienciaAcademicaModelSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = ExperienciaAcademicaFilterClass

    # Permissions:
    permission_classes = [ExperienciaAcademicaPermission]


class ExperienciaProfissionalModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return ExperienciaProfissional.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return ExperienciaProfissional.objects.filter(usuario=user)
        else:
            return ExperienciaProfissional.objects.all()

    serializer_class = ExperienciaProfissionalModelSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = ExperienciaProfissionalFilterClass

    # Permissions:
    permission_classes = [ExperienciaProfissionalPermission]


class IdiomaModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return Idioma.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return Idioma.objects.filter(usuario=user)
        else:
            return Idioma.objects.all()

    serializer_class = IdiomaModelSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = IdiomaFilterClass

    # Permissions:
    permission_classes = [IdiomaPermission]


class ConquistaModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return Conquista.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return Conquista.objects.filter(usuario=user)
        else:
            return Conquista.objects.all()

    serializer_class = ConquistaModelSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = ConquistaFilterClass

    # Permissions:
    permission_classes = [ConquistaPermission]


class CurriculoModelViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        # TODO: Documentação: Remover para o deploy
        # Para resolver erro do swagger e redoc sem alterar o sistema
        if is_swagger_request(self.request):
            return Curriculo.objects.all()

        user = self.request.user
        if user.tipo == "candidato":
            return Curriculo.objects.filter(usuario=user)
        else:
            return Curriculo.objects.all()

    serializer_class = CurriculoModelSerializer

    filter_backends = [RQLFilterBackend]
    rql_filter_class = CurriculoFilterClass

    # Permissions:
    permission_classes = [CurriculoPermission]
