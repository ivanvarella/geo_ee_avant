from rest_framework import serializers
from django.core.exceptions import ValidationError
import os
import uuid
from django.core.files.storage import default_storage
from candidatos.models import (
    Habilidade,
    ExperienciaAcademica,
    ExperienciaProfissional,
    Idioma,
    Conquista,
    Curriculo,
)


class ExperienciaAcademicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaAcademica
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
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


class ExperienciaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienciaProfissional
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
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


class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
            )

        # Verifica se já existe uma habilidade com o mesmo usuario e nome
        if Idioma.objects.filter(
            usuario=user, idioma=validated_data["idioma"]
        ).exists():
            raise serializers.ValidationError(
                "Esse idioma já foi cadastrado para este usuário."
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

        # Verifica se já existe um idioma com o mesmo usuario e idioma (excluindo o próprio registro)
        if (
            Idioma.objects.filter(
                usuario=instance.usuario, idioma=validated_data.get("idioma")
            )
            .exclude(id=instance.id)
            .exists()
        ):
            raise serializers.ValidationError(
                "Esse idioma já foi cadastrado para este usuário."
            )

        return super().update(
            instance, validated_data
        )  # Retorne a atualização padrão após verificar permissões


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
            )

        # Verifica se já existe uma habilidade com o mesmo usuario e nome
        if Habilidade.objects.filter(
            usuario=user, nome=validated_data["nome"]
        ).exists():
            raise serializers.ValidationError(
                "Essa habilidade já foi cadastrada para este usuário."
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

        # Verifica se já existe uma habilidade com o mesmo usuario e nome, excluindo o registro atual
        if (
            Habilidade.objects.filter(
                usuario=instance.usuario, nome=validated_data.get("nome")
            )
            .exclude(id=instance.id)
            .exists()
        ):
            raise serializers.ValidationError(
                "Essa habilidade já foi cadastrada para este usuário."
            )

        return super().update(
            instance, validated_data
        )  # Retorne a atualização padrão após verificar permissões


class ConquistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conquista
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def create(self, validated_data):
        user = self.context["request"].user

        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
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


class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = "__all__"
        read_only_fields = ["id", "usuario"]

    def validate_arquivo(self, value):
        # Verifica se a extensão do arquivo é permitida (PDF, DOC, DOCX)
        valid_extensions = ["pdf", "doc", "docx"]
        extension = value.name.split(".")[-1].lower()
        if extension not in valid_extensions:
            raise ValidationError("Arquivo deve ser um PDF, DOC ou DOCX.")
        return value

    def delete_file(self, arquivo):
        # Deleta o arquivo antigo usando o storage do Django, tentando caminhos alternativos se necessário
        try:
            storage = arquivo.storage
            file_path = arquivo.name  # Caminho relativo do arquivo
            if storage.exists(file_path):
                storage.delete(file_path)
            else:
                # Tenta deletar do caminho alternativo, se o arquivo não estiver no caminho original
                alt_path = f"curriculos/{arquivo.name}"
                if storage.exists(alt_path):
                    storage.delete(alt_path)
        except Exception as e:
            raise serializers.ValidationError(f"Erro ao deletar arquivo: {e}")

    def save_file(self, arquivo, nome_arquivo):
        # Salva o novo arquivo no diretório especificado e retorna o caminho relativo
        try:
            file_path = f"curriculos/{nome_arquivo}"
            with default_storage.open(file_path, "wb+") as destination:
                for chunk in arquivo.chunks():
                    destination.write(chunk)
            return file_path
        except Exception as e:
            raise serializers.ValidationError(f"Erro ao salvar arquivo: {e}")

    def create(self, validated_data):
        # Define o usuário autenticado como o dono dos dados, validando o tipo
        user = self.context["request"].user
        if user.tipo != "candidato":
            raise serializers.ValidationError(
                "Apenas usuários do tipo 'candidato' podem criar dados."
            )

        validated_data["usuario"] = user

        # Processa e salva o arquivo, gerando um nome único
        arquivo = validated_data.pop("arquivo")
        nome_arquivo = f"{user.id}_{uuid.uuid4()}.{arquivo.name.split('.')[-1]}"
        file_path = self.save_file(arquivo, nome_arquivo)
        validated_data["arquivo"] = file_path

        # Cria a instância do currículo no banco de dados
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Verifica se o usuário autenticado é o proprietário dos dados antes de atualizar
        if instance.usuario != self.context["request"].user:
            raise serializers.ValidationError(
                "Você não tem permissão para atualizar os dados."
            )

        arquivo = validated_data.get("arquivo", None)

        if arquivo:
            # Armazena o arquivo antigo para deletá-lo após salvar o novo
            arquivo_antigo = instance.arquivo

            # Gera um nome único para o novo arquivo e salva-o
            usuario = self.context["request"].user
            nome_arquivo = f"{usuario.id}_{uuid.uuid4()}.{arquivo.name.split('.')[-1]}"
            file_path = self.save_file(arquivo, nome_arquivo)
            validated_data["arquivo"] = file_path

            # Deleta o arquivo antigo após salvar o novo
            if arquivo_antigo:
                self.delete_file(arquivo_antigo)

        # Atualiza os dados no banco de dados
        return super().update(instance, validated_data)
