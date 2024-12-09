from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from candidatos.models import DadosCandidato

# Comando: python3 manage.py test candidatos.test_views


class DadosCandidatoViewSetTestCase(APITestCase):
    def setUp(self):
        # Criar um usuário de teste
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123",
            email="testuser@example.com",
            tipo="candidato",  # Certifique-se de que o campo "tipo" exista no modelo do usuário
        )

        # Criar DadosCandidato associado ao usuário
        self.dados_candidato = DadosCandidato.objects.create(
            usuario=self.user,
            genero="masculino",
            deficiencia=False,
            linkedin="https://www.linkedin.com/in/testuser",
            github="https://github.com/testuser",
        )

        # Obter um token de acesso JWT
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Configurar o cliente com autenticação
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_get_dados_candidatos(self):
        # Fazer a requisição GET
        response = self.client.get("/api/v1/dados_candidatos/")
        print(f"response.data: {response.data}")

        # Verificar o status HTTP
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar se os dados retornados estão corretos
        self.assertEqual(
            len(response.data["results"]), 1
        )  # Apenas um candidato criado no setup

        candidato = response.data["results"][0]
        self.assertEqual(candidato["usuario"], self.user.id)
        self.assertEqual(candidato["genero"], "masculino")
        self.assertEqual(candidato["linkedin"], "https://www.linkedin.com/in/testuser")
        self.assertEqual(candidato["github"], "https://github.com/testuser")
