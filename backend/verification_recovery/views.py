# Django DRF
from rest_framework import viewsets, mixins

# Serializers
from verification_recovery.serializers import (
    ResetarSenhaModelSerializer,
    ResetarSenhaCompletoModelSerializer,
    SolicitarTokenVerificacaoSerializer,
    ValidarTokenVerificacaoSerializer,
)

from rest_framework.decorators import action
from rest_framework.response import Response

# Permissões personalizadas
from verification_recovery.permissions import AllowAny

# Para garantir que cada ViewSet tenha seu respectivo Serializer
# corretamente implementado e com a lógica específica para cada
# operação (como POST, etc.), foram criados serializers diferentes
# para os seguintes casos, com as etapas no processo de redefinição de senha:
#
# 1 - Solicitar a redefinição de senha (envio de e-mail com o token):
#     O primeiro endpoint recebe o e-mail do usuário e, caso o e-mail seja
#     válido e o usuário esteja ativo, um token de redefinição de senha
#     é gerado e enviado para o endereço fornecido.
#
# 2 - Validar e redefinir a senha (validação do token e atualização da senha):
#     O segundo e último endpoint recebe o e-mail, o token e a nova senha.
#     Ele realiza a validação do token de forma segura, checando se é válido
#     e se ainda está dentro do prazo de validade (ex.: 2 horas).
#     Se todas as verificações forem bem-sucedidas, a senha do usuário é
#     redefinida.
#
# Com essa estrutura, o fluxo de recuperação de senha é simplificado para
# dois endpoints, garantindo segurança, eficiência e facilidade de manutenção
# sem a necessidade de um terceiro endpoint para validação intermediária do token.


class VerificacaoEmailViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"], url_path="enviar-token")
    def enviar_token(self, request):
        # Endpoint para solicitar envio do token
        serializer = SolicitarTokenVerificacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Token enviado para o e-mail."}, status=200)
        return Response(serializer.errors, status=400)

    @action(detail=False, methods=["post"], url_path="validar-token")
    def validar_token(self, request):
        # Endpoint para validar o token e confirmar o e-mail
        serializer = ValidarTokenVerificacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "E-mail verificado com sucesso!"}, status=200)
        return Response(serializer.errors, status=400)


# ViewSet para solicitar redefinição de senha
class ResetarSenhaModelViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ResetarSenhaModelSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Lógica personalizada para enviar o e-mail com o token de redefinição de senha
        return super().create(request, *args, **kwargs)


# ViewSet para confirmar o token e finalizar a redefinição de senha
class ResetarSenhaCompletoModelViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = ResetarSenhaCompletoModelSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Lógica para concluir o processo de redefinição e atualizar a senha
        return super().create(request, *args, **kwargs)
