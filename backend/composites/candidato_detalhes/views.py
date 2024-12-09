from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from candidatos.models import DadosCandidato
from shareds.models import Endereco, Telefone
from composites.candidato_detalhes.permissions import CandidatoDetalhesPermissions
from composites.candidato_detalhes.serializers import (
    DadosCandidatoSerializer,
    EnderecoSerializer,
    TelefoneSerializer,
)


class CandidatoDetalhesAPIView(APIView):
    # Define as permissões específicas para acessar este endpoint
    permission_classes = [CandidatoDetalhesPermissions]

    def get_queryset(self, user):
        """
        Método auxiliar para buscar os dados de acordo com o tipo de usuário.
        Assegura que apenas dados permitidos sejam retornados.
        """
        # Usuários administradores e funcionários têm acesso a todos os dados
        if user.tipo in ["administrador", "funcionario"]:
            dados_candidato_queryset = DadosCandidato.objects.all()
            endereco_queryset = Endereco.objects.all()
            telefone_queryset = Telefone.objects.all()
        # Candidatos e responsáveis só têm acesso aos próprios dados
        elif user.tipo in ["candidato", "responsavel"]:
            dados_candidato_queryset = DadosCandidato.objects.filter(usuario=user)
            endereco_queryset = Endereco.objects.filter(usuario=user)
            telefone_queryset = Telefone.objects.filter(usuario=user)
        # Qualquer outro tipo de usuário não terá acesso a dados
        else:
            dados_candidato_queryset = DadosCandidato.objects.none()
            endereco_queryset = Endereco.objects.none()
            telefone_queryset = Telefone.objects.none()

        return dados_candidato_queryset, endereco_queryset, telefone_queryset

    def get(self, request):
        user = self.request.user

        # Obtém os querysets de acordo com o usuário
        dados_candidato_queryset, endereco_queryset, telefone_queryset = (
            self.get_queryset(user)
        )

        # Serializa cada conjunto de dados individualmente
        dados_candidato_serializer = DadosCandidatoSerializer(
            dados_candidato_queryset, many=True
        )
        endereco_serializer = EnderecoSerializer(endereco_queryset, many=True)
        telefone_serializer = TelefoneSerializer(telefone_queryset, many=True)

        # Combina os dados serializados em um único dicionário para retornar
        response_data = {
            "dados_candidato": dados_candidato_serializer.data,
            "endereco": endereco_serializer.data,
            "telefones": telefone_serializer.data,
        }

        # Retorna a resposta com os dados serializados
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        # Recebe os dados enviados na requisição
        dados_candidato_data = request.data.get("dados_candidato")
        enderecos_data = request.data.get("enderecos")
        telefones_data = request.data.get("telefones", [])

        # Início do contexto atômico
        try:
            with transaction.atomic():
                # Criação de registros para DadosCandidato
                dados_candidato_serializer = DadosCandidatoSerializer(
                    data=dados_candidato_data, context={"request": request}
                )
                dados_candidato_serializer.is_valid(raise_exception=True)
                dados_candidato_serializer.save()

                # Criação de registros para Endereco
                endereco_serializer = EnderecoSerializer(
                    data=enderecos_data, context={"request": request}
                )
                endereco_serializer.is_valid(raise_exception=True)
                endereco_serializer.save()

                # Criação de registros para Telefone
                telefone_serializer = TelefoneSerializer(
                    data=telefones_data, many=True, context={"request": request}
                )
                telefone_serializer.is_valid(raise_exception=True)
                telefone_serializer.save()

            # Retorna os dados criados
            return Response(
                {
                    "dados_candidato": dados_candidato_serializer.data,
                    "endereco": endereco_serializer.data,
                    "telefones": telefone_serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            # Se ocorrer qualquer erro, a transação será revertida automaticamente
            return Response(
                {"detail": f"Ocorreu um erro ao tentar salvar os dados: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request):
        """
        Atualiza completamente os dados do candidato, endereço (único) e telefones (múltiplos).
        """
        user = request.user

        # Obtém os dados enviados no payload
        dados_candidato_data = request.data.get("dados_candidato", {})
        endereco_data = request.data.get("endereco", {})
        telefones_data = request.data.get("telefones", [])

        # Validações iniciais
        if not dados_candidato_data:
            return Response(
                {"detail": "Os dados do candidato são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not endereco_data:
            return Response(
                {"detail": "Os dados de endereço são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            with transaction.atomic():
                # Verifica se o usuário possui os dados básicos
                try:
                    dados_candidato_instance = DadosCandidato.objects.get(usuario=user)
                except DadosCandidato.DoesNotExist:
                    return Response(
                        {"detail": "Dados do candidato não encontrados."},
                        status=status.HTTP_404_NOT_FOUND,
                    )

                # Atualiza os dados do candidato
                dados_candidato_serializer = DadosCandidatoSerializer(
                    dados_candidato_instance,
                    data=dados_candidato_data,
                    context={"request": request},
                )
                dados_candidato_serializer.is_valid(raise_exception=True)
                dados_candidato_serializer.save()

                # Verifica ou cria o endereço
                endereco_instance = Endereco.objects.filter(usuario=user).first()
                if endereco_instance:
                    endereco_serializer = EnderecoSerializer(
                        endereco_instance,
                        data=endereco_data,
                        context={"request": request},
                    )
                else:
                    endereco_serializer = EnderecoSerializer(
                        data=endereco_data,
                        context={"request": request},
                    )
                endereco_serializer.is_valid(raise_exception=True)
                endereco_instance = endereco_serializer.save(usuario=user)

                # Atualiza ou cria os telefones
                telefone_ids_atualizados = []
                for telefone_data in telefones_data:
                    telefone_id = telefone_data.get("id")
                    if telefone_id:
                        # Valida se o telefone pertence ao usuário
                        telefone_instance = Telefone.objects.filter(
                            id=telefone_id, usuario=user
                        ).first()
                        if not telefone_instance:
                            return Response(
                                {
                                    "detail": f"Telefone com ID {telefone_id} não encontrado."
                                },
                                status=status.HTTP_404_NOT_FOUND,
                            )
                        telefone_serializer = TelefoneSerializer(
                            telefone_instance,
                            data=telefone_data,
                            context={"request": request},
                        )
                    else:
                        # Cria novo telefone
                        telefone_serializer = TelefoneSerializer(
                            data=telefone_data,
                            context={"request": request},
                        )
                    telefone_serializer.is_valid(raise_exception=True)
                    telefone_instance = telefone_serializer.save(usuario=user)
                    telefone_ids_atualizados.append(telefone_instance.id)

                # Exclui telefones não enviados no payload
                Telefone.objects.filter(usuario=user).exclude(
                    id__in=telefone_ids_atualizados
                ).delete()

            return Response(
                {
                    "dados_candidato": dados_candidato_serializer.data,
                    "endereco": EnderecoSerializer(
                        endereco_instance, context={"request": request}
                    ).data,
                    "telefones": [
                        TelefoneSerializer(t, context={"request": request}).data
                        for t in Telefone.objects.filter(usuario=user)
                    ],
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
        Atualiza parcialmente os dados do candidato, endereço (único) e telefones (múltiplos).
        """
        user = request.user

        # Obtém os dados enviados no payload
        dados_candidato_data = request.data.get("dados_candidato", {})
        endereco_data = request.data.get("endereco", {})
        telefones_data = request.data.get("telefones", [])

        try:
            with transaction.atomic():
                # Atualiza parcialmente os dados do candidato, se enviados
                if dados_candidato_data:
                    try:
                        dados_candidato_instance = DadosCandidato.objects.get(
                            usuario=user
                        )
                    except DadosCandidato.DoesNotExist:
                        return Response(
                            {"detail": "Dados do candidato não encontrados."},
                            status=status.HTTP_404_NOT_FOUND,
                        )
                    dados_candidato_serializer = DadosCandidatoSerializer(
                        dados_candidato_instance,
                        data=dados_candidato_data,
                        partial=True,
                        context={"request": request},
                    )
                    dados_candidato_serializer.is_valid(raise_exception=True)
                    dados_candidato_serializer.save()

                # Atualiza ou cria o endereço, se enviado
                if endereco_data:
                    endereco_instance = Endereco.objects.filter(usuario=user).first()
                    if endereco_instance:
                        endereco_serializer = EnderecoSerializer(
                            endereco_instance,
                            data=endereco_data,
                            partial=True,
                            context={"request": request},
                        )
                    else:
                        endereco_serializer = EnderecoSerializer(
                            data=endereco_data,
                            context={"request": request},
                        )
                    endereco_serializer.is_valid(raise_exception=True)
                    endereco_instance = endereco_serializer.save(usuario=user)

                # Atualiza ou cria os telefones, se enviados
                telefone_ids_atualizados = []
                for telefone_data in telefones_data:
                    telefone_id = telefone_data.get("id")
                    if telefone_id:
                        telefone_instance = Telefone.objects.filter(
                            id=telefone_id, usuario=user
                        ).first()
                        if not telefone_instance:
                            return Response(
                                {
                                    "detail": f"Telefone com ID {telefone_id} não encontrado."
                                },
                                status=status.HTTP_404_NOT_FOUND,
                            )
                        telefone_serializer = TelefoneSerializer(
                            telefone_instance,
                            data=telefone_data,
                            partial=True,
                            context={"request": request},
                        )
                    else:
                        telefone_serializer = TelefoneSerializer(
                            data=telefone_data,
                            context={"request": request},
                        )
                    telefone_serializer.is_valid(raise_exception=True)
                    telefone_instance = telefone_serializer.save(usuario=user)
                    telefone_ids_atualizados.append(telefone_instance.id)

                # Exclui telefones não enviados no payload
                Telefone.objects.filter(usuario=user).exclude(
                    id__in=telefone_ids_atualizados
                ).delete()

            return Response(
                {
                    "dados_candidato": (
                        dados_candidato_serializer.data if dados_candidato_data else {}
                    ),
                    "endereco": (
                        EnderecoSerializer(
                            endereco_instance, context={"request": request}
                        ).data
                        if endereco_data
                        else {}
                    ),
                    "telefones": [
                        TelefoneSerializer(t, context={"request": request}).data
                        for t in Telefone.objects.filter(usuario=user)
                    ],
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"detail": f"Erro ao atualizar parcialmente os dados: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST,
            )
