from rest_framework import serializers
from empresas.models import Empresa
from django.core.exceptions import ValidationError
import os
import uuid
from django.core.files.storage import default_storage

import logging

logger = logging.getLogger(__name__)


# TODO: Remover comentários
# 1- Cada usuário (somente tipo == "responsavel") só pode ter uma empresa atrelada, bloquear isso
class EmpresaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"
        read_only_fields = ["id", "responsavel"]

    def validate_logo(self, value):
        # Verifica se a extensão do arquivo é uma imagem permitida (PNG, JPG, JPEG)
        valid_extensions = ["png", "jpg", "jpeg"]
        extension = value.name.split(".")[-1].lower()
        if extension not in valid_extensions:
            raise serializers.ValidationError(
                "Arquivo de logo deve ser uma imagem PNG, JPG ou JPEG."
            )
        return value

    def validate_banner(self, value):
        # Verifica se a extensão do arquivo é uma imagem permitida (PNG, JPG, JPEG)
        valid_extensions = ["png", "jpg", "jpeg"]
        extension = value.name.split(".")[-1].lower()
        if extension not in valid_extensions:
            raise serializers.ValidationError(
                "Arquivo de banner deve ser uma imagem PNG, JPG ou JPEG."
            )
        return value

    def delete_file(self, arquivo, field_name):
        try:
            storage = arquivo.storage
            file_path = arquivo.name  # Caminho relativo do arquivo
            logger.debug(f"Tentando deletar arquivo '{field_name}': {file_path}")
            if storage.exists(file_path):
                storage.delete(file_path)
                logger.info(f"Arquivo '{field_name}' deletado com sucesso: {file_path}")
            else:
                logger.warning(
                    f"Arquivo '{field_name}' não encontrado no caminho: {file_path}"
                )
        except Exception as e:
            logger.error(f"Erro ao deletar arquivo '{field_name}': {e}")
            raise serializers.ValidationError(
                f"Erro ao deletar arquivo '{field_name}': {e}"
            )

    def save_file(self, arquivo, nome_arquivo, field_name):
        try:
            file_path = f"{field_name}/{nome_arquivo}"
            with default_storage.open(file_path, "wb+") as destination:
                for chunk in arquivo.chunks():
                    destination.write(chunk)
            logger.info(f"Arquivo '{field_name}' salvo com sucesso: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Erro ao salvar arquivo '{field_name}': {e}")
            raise serializers.ValidationError(
                f"Erro ao salvar arquivo '{field_name}': {e}"
            )

    def create(self, validated_data):
        user = self.context["request"].user

        # Verifica se o usuário já possui uma empresa
        if Empresa.objects.filter(responsavel=user).exists():
            raise serializers.ValidationError(
                "Você já está cadastrado como responsável por uma empresa. Não é possível criar uma nova empresa enquanto."
            )

        # Adiciona o usuário autenticado ao campo `responsavel`
        validated_data["responsavel"] = user

        # Processa e salva o logo
        logo = validated_data.pop("logo", None)
        if logo:
            nome_logo = f"{user.id}_{uuid.uuid4()}.{logo.name.split('.')[-1]}"
            validated_data["logo"] = self.save_file(logo, nome_logo, "empresas_logos")

        # Processa e salva o banner
        banner = validated_data.pop("banner", None)
        if banner:
            nome_banner = f"{user.id}_{uuid.uuid4()}.{banner.name.split('.')[-1]}"
            validated_data["banner"] = self.save_file(
                banner, nome_banner, "empresas_banners"
            )

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Verifica se o usuário autenticado é o responsável pela empresa
        if instance.responsavel != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar esta empresa."
            )

        # Processa e salva o novo logo, se fornecido
        logo = validated_data.pop("logo", None)
        if logo:
            # Deleta o logo antigo, se existir
            if instance.logo:
                self.delete_file(instance.logo, "logo")

            # Salva o novo logo
            nome_logo = (
                f"{instance.responsavel.id}_{uuid.uuid4()}.{logo.name.split('.')[-1]}"
            )
            validated_data["logo"] = self.save_file(logo, nome_logo, "empresas_logos")

        # Processa e salva o novo banner, se fornecido
        banner = validated_data.pop("banner", None)
        if banner:
            # Deleta o banner antigo, se existir
            if instance.banner:
                self.delete_file(instance.banner, "banner")

            # Salva o novo banner
            nome_banner = (
                f"{instance.responsavel.id}_{uuid.uuid4()}.{banner.name.split('.')[-1]}"
            )
            validated_data["banner"] = self.save_file(
                banner, nome_banner, "empresas_banners"
            )

        return super().update(
            instance, validated_data
        )  # Retorne a atualização padrão após verificar permissões

    # TODO: Acho que isso deveria ou poderia ser feito de outra forma...
    def delete_instance(self, instance):
        request = self.context.get("request")
        user = request.user

        # Verifica se a vaga pertence à empresa do usuário logado antes de deletar
        if instance.responsavel != user:
            raise serializers.ValidationError(
                "Você não tem permissão para deletar esta vaga."
            )

        instance.delete()
