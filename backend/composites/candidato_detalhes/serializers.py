from rest_framework import serializers
from candidatos.models import DadosCandidato
from shareds.models import Endereco, Telefone
from django.core.exceptions import ValidationError


# Serializador para DadosCandidato
class DadosCandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosCandidato
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        # Verifica se o usuário tem permissão para criar um registro
        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
            )

        # Permitir apenas um registro por usuário
        if DadosCandidato.objects.filter(usuario=user).exists():
            raise serializers.ValidationError(
                "Você já cadastrou seus dados referente a esta parte do cadastro."
            )

        # Adiciona o usuário autenticado ao campo `usuario`
        validated_data["usuario"] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Garante que o usuário autenticado é o "dono" do registro
        if instance.usuario != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar os dados."
            )

        return super().update(instance, validated_data)


# Serializador para Endereco
class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        # Permitir apenas um registro por usuário
        if Endereco.objects.filter(usuario=user).exists():
            raise serializers.ValidationError("Você já cadastrou um endereço.")

        # Adiciona o usuário autenticado ao campo `usuario`
        validated_data["usuario"] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Garante que o usuário autenticado é o "dono" do registro
        if instance.usuario != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar os dados."
            )

        return super().update(instance, validated_data)


# Serializador para Telefone
class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        # Limita o número de telefones por usuário a no máximo 3
        if Telefone.objects.filter(usuario=user).count() >= 3:
            raise serializers.ValidationError(
                "Você já cadastrou o máximo de 3 telefones."
            )

        # Adiciona o usuário autenticado ao campo `usuario`
        validated_data["usuario"] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Garante que o usuário autenticado é o "dono" do registro
        if instance.usuario != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar os dados."
            )

        return super().update(instance, validated_data)
