from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from vagas.models import Vaga, Candidatura
from empresas.models import Empresa

# TODO: Remover comentários
# O que é preciso implementar:
# 1- Verificar se o usuário logado tem o tipo responsavel.
# 2- Obter a empresa que tem o usuário logado como responsavel.
#   2.1 - Não permitir a criação da vaga caso o usuário logado (mesmo sendo um responsavel) não possua
# uma empresa atrelada, ou seja, realizou o cadastro no sistema como reposável mas ainda não criou a empresa atrelada à sua conta.
# 3- Caso possua empresa atrelada, atribuir essa empresa automaticamente ao campo empresa da vaga antes de salvá-la, restrigindo com que outros usuários possam criar vagas para outras emrpesas que não as suas.
# 4- Restringir a criação e atualização de vagas a apenas usuários responsáveis pela empresa.


class VagaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = "__all__"
        read_only_fields = ["id", "empresa"]

    def validate(self, data):
        request = self.context.get("request")
        user = request.user

        # Regra 1: Verifica se o usuário logado é do tipo "responsavel"
        if user.tipo != "responsavel":
            raise ValidationError(
                "Somente usuários responsáveis pela empresa podem criar ou atualizar suas vagas."
            )

        # Regra 2 e 2.1: Obtém a empresa associada ao responsável e verifica se ele possui uma empresa atrelada
        try:
            empresa = Empresa.objects.get(responsavel=user)
        except Empresa.DoesNotExist:
            raise ValidationError(
                "Este usuário responsável não possui uma empresa associada. "
                "É necessário possuir uma empresa associada à sua conta antes de cadastrar uma vaga."
            )

        # Regra 3: Atribui automaticamente a empresa ao campo "empresa"
        data["empresa"] = empresa
        return data

    def create(self, validated_data):
        # Com a empresa já definida na validação, prossegue para criar a vaga
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user

        # Verifica se a vaga pertence à empresa do usuário logado antes de atualizar
        if instance.empresa.responsavel != user:
            raise ValidationError("Você não tem permissão para atualizar esta vaga.")

        return super().update(instance, validated_data)

    def delete_instance(self, instance):
        request = self.context.get("request")
        user = request.user

        # Verifica se a vaga pertence à empresa do usuário logado antes de deletar
        if instance.empresa.responsavel != user:
            raise ValidationError("Você não tem permissão para deletar esta vaga.")

        instance.delete()


class CandidaturaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidatura
        fields = "__all__"
        read_only_fields = ["id", "data_candidatura", "usuario"]

    def create(self, validated_data):
        vaga = validated_data.get("vaga")
        validated_data["status"] = "PENDENTE"

        # Verifica se a vaga foi passada
        if not vaga:
            raise ValidationError("A vaga é obrigatória para criar uma candidatura.")

        # Verifica se o usuário é do tipo "candidato"
        if self.context.get("request").user.tipo != "candidato":
            raise ValidationError("Apenas candidatos possuem acesso.")

        # Verifica se o candidato já se inscreveu para esta vaga
        if Candidatura.objects.filter(
            vaga=vaga, usuario=self.context.get("request").user
        ).exists():
            raise ValidationError("Você já se inscreveu para esta vaga.")

        # Usuáio sempre será o usuário autenticado - após todas as verificações
        validated_data["usuario"] = self.context.get("request").user

        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user
        # Verifica se o usuário autenticado (user) = usuario tabela (instance.usuario)
        is_candidate = instance.usuario == user

        # Verifica se o usuario autenticado (user) = responsavel -> empresa -> vaga -> candidatura
        is_responsavel = instance.vaga.empresa.responsavel == user
        new_status = validated_data.get("status")

        # Força os valores de 'usuario' e 'vaga' para os existentes na instância, ou seja, os mesmos do banco
        validated_data["usuario"] = instance.usuario
        validated_data["vaga"] = instance.vaga

        # Verifica se o usuário é o candidato dono da candidatura ou se é responsável pela empresa associada à vaga
        # Lógica esperada:
        # 1- O candidato que se candidatou para esta vaga pode alterar somente para "CANCELADO" ou "PENDENTE", é como se retirasse sua candidatura à vaga (cancelado) ou colocasse novamente (pendente).
        # 2- O responsavel da empresa (dessa vaga) pode alterar após a candidatura do candidato somente para "APROVADO" ou "REJEITADO".
        # 3- Outros usuários (que não os candidatos que criaram essa candidatura e os responsaveis das empresas dessa vaga,
        # que está relacionada a essa candidatura -> ufaaa...) não podem alterar as candidaturas.
        if (
            is_candidate
            and user.tipo == "candidato"
            and new_status in ["CANCELADO", "PENDENTE"]
        ):
            return super().update(instance, validated_data)

        if is_responsavel and new_status in ["APROVADO", "REJEITADO"]:
            return super().update(instance, validated_data)

        raise ValidationError("Você não tem permissão para atualizar esta candidatura.")
