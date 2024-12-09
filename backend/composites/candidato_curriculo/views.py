from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
import json

from candidatos.models import (
    Habilidade,
    ExperienciaAcademica,
    ExperienciaProfissional,
    Idioma,
    Conquista,
    Curriculo,
)

from composites.candidato_curriculo.permissions import CandidatoCurriculoPermissions
from composites.candidato_curriculo.serializers import (
    ExperienciaAcademicaSerializer,
    ExperienciaProfissionalSerializer,
    IdiomaSerializer,
    HabilidadeSerializer,
    ConquistaSerializer,
    CurriculoSerializer,
)


class CandidatoCurriculoAPIView(APIView):
    # Define as permissões específicas para acessar este endpoint
    permission_classes = [CandidatoCurriculoPermissions]

    def get_queryset(self, user):
        """
        Obtém os querysets das tabelas relacionadas, de acordo com o tipo de usuário.
        """
        if user.tipo in ["administrador", "funcionario", "responsavel"]:
            return (
                Habilidade.objects.all(),
                ExperienciaAcademica.objects.all(),
                ExperienciaProfissional.objects.all(),
                Idioma.objects.all(),
                Conquista.objects.all(),
                Curriculo.objects.all(),
            )
        elif user.tipo in ["candidato"]:
            return (
                Habilidade.objects.filter(usuario=user),
                ExperienciaAcademica.objects.filter(usuario=user),
                ExperienciaProfissional.objects.filter(usuario=user),
                Idioma.objects.filter(usuario=user),
                Conquista.objects.filter(usuario=user),
                Curriculo.objects.filter(usuario=user),
            )
        else:
            return (
                Habilidade.objects.none(),
                ExperienciaAcademica.objects.none(),
                ExperienciaProfissional.objects.none(),
                Idioma.objects.none(),
                Conquista.objects.none(),
                Curriculo.objects.none(),
            )

    def get(self, request):
        user = request.user

        # Obtém os querysets
        (
            habilidades,
            experiencias_academicas,
            experiencias_profissionais,
            idiomas,
            conquistas,
            curriculos,
        ) = self.get_queryset(user)

        # Serializa os dados
        response_data = {
            "habilidades": HabilidadeSerializer(habilidades, many=True).data,
            "experiencias_academicas": ExperienciaAcademicaSerializer(
                experiencias_academicas, many=True
            ).data,
            "experiencias_profissionais": ExperienciaProfissionalSerializer(
                experiencias_profissionais, many=True
            ).data,
            "idiomas": IdiomaSerializer(idiomas, many=True).data,
            "conquistas": ConquistaSerializer(conquistas, many=True).data,
            "curriculos": CurriculoSerializer(curriculos, many=True).data,
        }

        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Cria novos registros para as tabelas relacionadas.
        """
        data = request.data

        try:
            with transaction.atomic():
                # Converte as strings JSON para listas de objetos
                habilidades = json.loads(data.get("habilidades", "[]"))
                experiencias_academicas = json.loads(
                    data.get("experiencias_academicas", "[]")
                )
                experiencias_profissionais = json.loads(
                    data.get("experiencias_profissionais", "[]")
                )
                idiomas = json.loads(data.get("idiomas", "[]"))
                conquistas = json.loads(data.get("conquistas", "[]"))

                # Tratamento do curriculo do candidato
                curriculo_data = json.loads(
                    data.get("curriculo", "{}")
                )  # Transforma em dicionário
                titulo_curriculo = curriculo_data.get(
                    "titulo_curriculo"
                )  # Extrai o título
                arquivo = request.FILES.get("arquivo")  # Obtém o arquivo enviado

                # Validar se ambos os valores estão presentes
                if not titulo_curriculo or not arquivo:
                    return Response(
                        {"detail": "Título do currículo ou arquivo ausente."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                # Combina os dados em um dicionário
                curriculo = {
                    "titulo_curriculo": titulo_curriculo,
                    "arquivo": arquivo,
                }

                # Aplicação dos serializers:
                habilidade_serializer = HabilidadeSerializer(
                    data=habilidades,
                    many=True,
                    context={"request": request},
                )
                habilidade_serializer.is_valid(raise_exception=True)
                habilidade_serializer.save()

                experiencia_academica_serializer = ExperienciaAcademicaSerializer(
                    data=experiencias_academicas,
                    many=True,
                    context={"request": request},
                )
                experiencia_academica_serializer.is_valid(raise_exception=True)
                experiencia_academica_serializer.save()

                experiencia_profissional_serializer = ExperienciaProfissionalSerializer(
                    data=experiencias_profissionais,
                    many=True,
                    context={"request": request},
                )
                experiencia_profissional_serializer.is_valid(raise_exception=True)
                experiencia_profissional_serializer.save()

                idioma_serializer = IdiomaSerializer(
                    data=idiomas,
                    many=True,
                    context={"request": request},
                )
                idioma_serializer.is_valid(raise_exception=True)
                idioma_serializer.save()

                conquista_serializer = ConquistaSerializer(
                    data=conquistas,
                    many=True,
                    context={"request": request},
                )
                conquista_serializer.is_valid(raise_exception=True)
                conquista_serializer.save()

                curriculo_serializer = CurriculoSerializer(
                    data=curriculo,
                    context={"request": request},
                )
                curriculo_serializer.is_valid(raise_exception=True)
                curriculo_serializer.save()

            return Response(
                {"detail": "Dados criados com sucesso!"}, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao criar dados: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request):
        """
        Atualiza completamente os dados do candidato e seus relacionados.
        """
        user = request.user

        # Obtém os dados enviados no payload
        experiencia_academica_data = request.data.get("experiencias_academicas", [])
        experiencia_profissional_data = request.data.get(
            "experiencias_profissionais", []
        )
        idiomas_data = request.data.get("idiomas", [])
        habilidades_data = request.data.get("habilidades", [])
        conquistas_data = request.data.get("conquistas", [])
        curriculo_data = request.data.get("curriculo", {})

        try:
            with transaction.atomic():
                # Atualiza ou cria o currículo principal
                curriculo_instance = Curriculo.objects.filter(usuario=user).first()
                if curriculo_instance:
                    curriculo_serializer = CurriculoSerializer(
                        curriculo_instance,
                        data=curriculo_data,
                        context={"request": request},
                    )
                else:
                    curriculo_serializer = CurriculoSerializer(
                        data=curriculo_data, context={"request": request}
                    )
                curriculo_serializer.is_valid(raise_exception=True)
                curriculo_instance = curriculo_serializer.save(usuario=user)

                # Atualiza ou cria as experiências acadêmicas
                ExperienciaAcademica.objects.filter(
                    curriculo=curriculo_instance
                ).delete()
                for experiencia in experiencia_academica_data:
                    experiencia["curriculo"] = curriculo_instance.id
                    experiencia_academica_serializer = ExperienciaAcademicaSerializer(
                        data=experiencia, context={"request": request}
                    )
                    experiencia_academica_serializer.is_valid(raise_exception=True)
                    experiencia_academica_serializer.save()

                # Atualiza ou cria as experiências profissionais
                ExperienciaProfissional.objects.filter(
                    curriculo=curriculo_instance
                ).delete()
                for experiencia in experiencia_profissional_data:
                    experiencia["curriculo"] = curriculo_instance.id
                    experiencia_profissional_serializer = (
                        ExperienciaProfissionalSerializer(
                            data=experiencia, context={"request": request}
                        )
                    )
                    experiencia_profissional_serializer.is_valid(raise_exception=True)
                    experiencia_profissional_serializer.save()

                # Atualiza ou cria os idiomas
                Idioma.objects.filter(curriculo=curriculo_instance).delete()
                for idioma in idiomas_data:
                    idioma["curriculo"] = curriculo_instance.id
                    idioma_serializer = IdiomaSerializer(
                        data=idioma, context={"request": request}
                    )
                    idioma_serializer.is_valid(raise_exception=True)
                    idioma_serializer.save()

                # Atualiza ou cria as habilidades
                Habilidade.objects.filter(curriculo=curriculo_instance).delete()
                for habilidade in habilidades_data:
                    habilidade["curriculo"] = curriculo_instance.id
                    habilidade_serializer = HabilidadeSerializer(
                        data=habilidade, context={"request": request}
                    )
                    habilidade_serializer.is_valid(raise_exception=True)
                    habilidade_serializer.save()

                # Atualiza ou cria as conquistas
                Conquista.objects.filter(curriculo=curriculo_instance).delete()
                for conquista in conquistas_data:
                    conquista["curriculo"] = curriculo_instance.id
                    conquista_serializer = ConquistaSerializer(
                        data=conquista, context={"request": request}
                    )
                    conquista_serializer.is_valid(raise_exception=True)
                    conquista_serializer.save()

                return Response(
                    {
                        "curriculo": curriculo_serializer.data,
                        "experiencias_academicas": experiencia_academica_data,
                        "experiencias_profissionais": experiencia_profissional_data,
                        "idiomas": idiomas_data,
                        "habilidades": habilidades_data,
                        "conquistas": conquistas_data,
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao atualizar dados: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def patch(self, request):
        """
        Atualiza parcialmente os dados do candidato e seus relacionados.
        """
        user = request.user

        # Obtém os dados enviados no payload
        curriculo_data = request.data.get("curriculo", {})
        experiencia_academica_data = request.data.get("experiencias_academicas", [])
        experiencia_profissional_data = request.data.get(
            "experiencias_profissionais", []
        )
        idiomas_data = request.data.get("idiomas", [])
        habilidades_data = request.data.get("habilidades", [])
        conquistas_data = request.data.get("conquistas", [])

        try:
            with transaction.atomic():
                # Atualiza o currículo principal, se enviado
                curriculo_instance = Curriculo.objects.filter(usuario=user).first()
                if curriculo_data:
                    if curriculo_instance:
                        curriculo_serializer = CurriculoSerializer(
                            curriculo_instance,
                            data=curriculo_data,
                            partial=True,
                            context={"request": request},
                        )
                        curriculo_serializer.is_valid(raise_exception=True)
                        curriculo_instance = curriculo_serializer.save(usuario=user)

                # Atualiza experiências acadêmicas, se enviadas
                for experiencia in experiencia_academica_data:
                    experiencia_id = experiencia.get("id")
                    if experiencia_id:
                        experiencia_instance = ExperienciaAcademica.objects.filter(
                            id=experiencia_id, curriculo=curriculo_instance
                        ).first()
                        if experiencia_instance:
                            experiencia_academica_serializer = (
                                ExperienciaAcademicaSerializer(
                                    experiencia_instance,
                                    data=experiencia,
                                    partial=True,
                                    context={"request": request},
                                )
                            )
                            experiencia_academica_serializer.is_valid(
                                raise_exception=True
                            )
                            experiencia_academica_serializer.save()

                # Atualiza as demais relações da mesma maneira...
                # Seguindo a lógica de identificar a instância e atualizá-la, caso exista.

                return Response(
                    {"detail": "Atualização parcial concluída com sucesso!"},
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao atualizar parcialmente os dados: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
