from django.urls import path, include
from rest_framework.routers import DefaultRouter
from verification_recovery.views import (
    ResetarSenhaModelViewSet,
    ResetarSenhaCompletoModelViewSet,
    VerificacaoEmailViewSet,
)


router = DefaultRouter()

router.register("resetar-senha", ResetarSenhaModelViewSet, basename="resetar_senha")

router.register(
    "resetar-senha/completo",
    ResetarSenhaCompletoModelViewSet,
    basename="resetar_senha_completo",
)

router.register("verificar-email", VerificacaoEmailViewSet, basename="verificar_email")


# Registra para o Django usar como path do sistema
urlpatterns = [
    path("", include(router.urls)),
]
