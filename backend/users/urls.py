from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import (
    CandidatoUserModelViewSet,
    AdminUserModelViewSet,
    FuncionarioUserModelViewSet,
    ResponsavelUserModelViewSet,
)

router = DefaultRouter()
router.register(
    "candidato", CandidatoUserModelViewSet, basename="candidato"
)  # Rota -> end point
router.register("funcionario", FuncionarioUserModelViewSet, basename="funcionario")
router.register("responsavel", ResponsavelUserModelViewSet, basename="responsavel")
router.register("admin", AdminUserModelViewSet, basename="admin")


# Registra para o Django usar como path do sistema
urlpatterns = [
    path("", include(router.urls)),
]
