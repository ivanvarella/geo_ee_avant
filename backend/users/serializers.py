from rest_framework import serializers
from users.models import CustomUser


# TODO: Verificar serializers de Candidato
class CandidatoUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "last_login",
            "is_superuser",
            "is_staff",
            "date_joined",
            "groups",
            "user_permissions",
        ]  # Oculta esses campos
        read_only_fields = [
            "id",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active",
            "tipo",
        ]

    def create(self, validated_data):
        validated_data["is_staff"] = False
        validated_data["is_superuser"] = False
        validated_data["is_active"] = True
        validated_data["tipo"] = "candidato"

        user = CustomUser(**validated_data)
        user.set_password(
            validated_data["password"]
        )  # Encrypts the password before saving
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data["is_staff"] = False
        validated_data["is_superuser"] = False
        validated_data["tipo"] = "candidato"

        # Checks if the password was provided in the update payload
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)  # Encrypts the new password

        # Updates the remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()  # Saves the changes to the database
        return instance


# TODO: Verificar serializers de Funcionario
class FuncionarioUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "last_login",
            "is_superuser",
            "is_staff",
            "date_joined",
            "groups",
            "user_permissions",
        ]  # Oculta esses campos
        read_only_fields = [
            "id",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active",
            "tipo",
        ]

    def create(self, validated_data):
        validated_data["is_staff"] = True
        validated_data["is_superuser"] = False
        validated_data["is_active"] = True
        validated_data["tipo"] = "funcionario"

        user = CustomUser(**validated_data)
        user.set_password(
            validated_data["password"]
        )  # Encrypts the password before saving
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data["is_staff"] = True
        validated_data["is_superuser"] = False
        validated_data["tipo"] = "funcionario"

        # Checks if the password was provided in the update payload
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)  # Encrypts the new password

        # Updates the remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()  # Saves the changes to the database
        return instance


# TODO: Verificar serializers de Responsavel
class ResponsavelUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "last_login",
            "is_superuser",
            "is_staff",
            "date_joined",
            "groups",
            "user_permissions",
        ]  # Oculta esses campos
        read_only_fields = [
            "id",
            "date_joined",
            "is_superuser",
            "is_staff",
            "is_active",
            "tipo",
        ]

    def create(self, validated_data):
        validated_data["is_staff"] = False
        validated_data["is_superuser"] = False
        validated_data["is_active"] = True
        validated_data["tipo"] = "responsavel"

        user = CustomUser(**validated_data)
        user.set_password(
            validated_data["password"]
        )  # Encrypts the password before saving
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data["is_staff"] = False
        validated_data["is_superuser"] = False
        validated_data["tipo"] = "responsavel"

        # Checks if the password was provided in the update payload
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)  # Encrypts the new password

        # Updates the remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()  # Saves the changes to the database
        return instance


# TODO: Verificar serializers de Admin
class AdminUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = [
            "groups",
            "user_permissions",
        ]  # Oculta esses campos

    def create(self, validated_data):
        validated_data["is_staff"] = True
        validated_data["is_superuser"] = True
        validated_data["is_active"] = True
        validated_data["tipo"] = "admin"

        user = CustomUser(**validated_data)
        user.set_password(
            validated_data["password"]
        )  # Encrypts the password before saving
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data["is_staff"] = True
        validated_data["is_superuser"] = True
        validated_data["tipo"] = "admin"

        # Checks if the password was provided in the update payload
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)  # Encrypts the new password

        # Updates the remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()  # Saves the changes to the database
        return instance
