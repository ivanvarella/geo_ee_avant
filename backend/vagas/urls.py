from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vagas.views import VagaModelViewSet, CandidaturaModelViewSet

router = DefaultRouter()
router.register("vagas", VagaModelViewSet)  # Rota -> end point
router.register("candidaturas", CandidaturaModelViewSet, basename="candidatura")


# Registra para o Django usar como path do sistema
urlpatterns = [
    path("", include(router.urls)),
]
