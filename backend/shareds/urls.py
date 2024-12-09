from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shareds.views import (
    EnderecoModelViewSet,
    TelefoneModelViewSet,
    CepSourceApiModelViewSet,
)

router = DefaultRouter()
router.register(
    "enderecos", EnderecoModelViewSet, basename="endereco"
)  # Rota -> end point
router.register("telefones", TelefoneModelViewSet, basename="telefone")
router.register("via-cep", CepSourceApiModelViewSet, basename="cepsourceapi")


urlpatterns = [
    path("", include(router.urls)),
]
