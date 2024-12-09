from django.urls import path, include
from rest_framework.routers import DefaultRouter
from empresas.views import EmpresaModelViewSet

router = DefaultRouter()
router.register("empresas", EmpresaModelViewSet)  # Rota -> end point


# Registra para o Django usar como path do sistema
urlpatterns = [
    path("", include(router.urls)),
]
