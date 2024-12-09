from django.urls import path, include
from rest_framework.routers import DefaultRouter
from candidatos.views import (
    DadosCandidatoModelViewSet,
    HabilidadeModelViewSet,
    ExperienciaAcademicaModelViewSet,
    ExperienciaProfissionalModelViewSet,
    IdiomaModelViewSet,
    ConquistaModelViewSet,
    CurriculoModelViewSet,
)

router = DefaultRouter()
router.register(
    "dados_candidatos", DadosCandidatoModelViewSet, basename="dadoscandidato"
)  # Rota -> end point
router.register("habilidades", HabilidadeModelViewSet, basename="habilidade")
router.register(
    "experiencia_academicas",
    ExperienciaAcademicaModelViewSet,
    basename="experienciaacademica",
)
router.register(
    "experiencia_profissionals",
    ExperienciaProfissionalModelViewSet,
    basename="experienciaprofissional",
)
router.register("idiomas", IdiomaModelViewSet, basename="idioma")
router.register("conquistas", ConquistaModelViewSet, basename="conquista")
router.register("curriculos", CurriculoModelViewSet, basename="curriculo")

# Registra para o Django usar como path do sistema
urlpatterns = [
    path("", include(router.urls)),
]
