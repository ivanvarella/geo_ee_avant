from rest_framework import serializers
from shareds.models import Endereco, Telefone, CepSourceApi


class EnderecoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"
        read_only_fields = ["id", "usuario_id"]

    def create(self, validated_data):

        user = self.context["request"].user

        # Só um endereço por usuário
        if Endereco.objects.filter(usuario=user).exists():
            raise serializers.ValidationError("Você já cadastrou um endereço.")

        # Adiciona o usuário autenticado ao campo `usuario`
        validated_data["usuario"] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Verifica se o usuário autenticado é o "dono" do campo na tabela
        if instance.usuario != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar os dados."
            )

        return super().update(
            instance, validated_data
        )  # Retorne a atualização padrão após verificar permissões


class TelefoneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = "__all__"
        read_only_fields = ["id", "usuario_id"]

    def create(self, validated_data):

        user = self.context["request"].user

        # Só 3 telefones por usuário
        if Telefone.objects.filter(usuario=user).count() >= 3:
            raise serializers.ValidationError(
                "Você já cadastrou o máximo de 3 telefones."
            )

        # Adiciona o usuário autenticado ao campo `usuario`
        validated_data["usuario"] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Verifica se o usuário autenticado é o "dono" do campo na tabela
        if instance.usuario != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar os dados."
            )

        return super().update(
            instance, validated_data
        )  # Retorne a atualização padrão após verificar permissões


class CepSourceApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CepSourceApi
        exclude = [
            "criado_em",
        ]
        read_only_fields = ["id"]
