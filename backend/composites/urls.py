from django.urls import path
from composites.candidato_detalhes.views import CandidatoDetalhesAPIView
from composites.candidato_curriculo.views import CandidatoCurriculoAPIView

urlpatterns = [
    # Rota para listar e criar "candidato_detalhes"
    path(
        "candidato-detalhes/",
        CandidatoDetalhesAPIView.as_view(),
        name="candidato_detalhes_list_create",
    ),
    # Rota para listar e criar "candidato_curriculo"
    path(
        "candidato-curriculo/",
        CandidatoCurriculoAPIView.as_view(),
        name="candidato_curriculo_list_create",
    ),
]
