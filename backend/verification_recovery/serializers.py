from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

User = get_user_model()


class SolicitarTokenVerificacaoSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if not user.is_active:
                raise serializers.ValidationError("Usuário inativo.")
            if user.is_email_verified:
                raise serializers.ValidationError("E-mail já verificado.")
        except User.DoesNotExist:
            raise serializers.ValidationError("E-mail não encontrado.")
        return value

    def save(self):
        user = User.objects.get(email=self.validated_data["email"])
        token = default_token_generator.make_token(user)
        expiration_time = timezone.now() + timedelta(hours=24)  # Token válido por 1 dia

        # Cria a URL para o frontend React
        verification_url = (
            f"{settings.FRONTEND_URL}/verificar-email/?token={token}&email={user.email}"
        )

        # Envia o e-mail com o link de verificação
        send_mail(
            subject="Verificação de E-mail",
            message=f"Olá {user.first_name} {user.last_name},\n\nPara verificar seu e-mail, clique no link abaixo:\n\n"
            f"{verification_url}",
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return user


class ValidarTokenVerificacaoSerializer(serializers.Serializer):
    token = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, data):
        token = data.get("token")
        email = data.get("email")

        try:
            user = User.objects.get(email=email)

            # Verifica se o usuário está ativo
            if not user.is_active:
                raise serializers.ValidationError("Usuário inativo.")

            # Verifica se o e-mail já foi verificado
            if user.is_email_verified:
                raise serializers.ValidationError("E-mail já verificado.")

            # Verifica se o token é válido
            if not default_token_generator.check_token(user, token):
                raise serializers.ValidationError("Token inválido ou expirado.")

            self.user = user  # Garantindo que a validação foi bem-sucedida antes de atribuir o usuário.

        except User.DoesNotExist:
            raise serializers.ValidationError("E-mail não encontrado.")

        return data

    def save(self):
        user = self.user
        user.is_email_verified = True
        user.save()
        return user


class ResetarSenhaModelSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value)
            # Verifica se o usuário está ativo
            if not self.user.is_active:
                raise serializers.ValidationError(
                    "Este e-mail está registrado, mas o usuário está inativo."
                )
        except User.DoesNotExist:
            raise serializers.ValidationError("Este e-mail não está registrado.")
        return value

    def save(self):
        user = self.user
        token = default_token_generator.make_token(user)  # Gera o token de redefinição

        # Envia o e-mail de recuperação com o token
        send_mail(
            subject="Código para redefinição de senha",
            message=f"Olá {user.first_name} {user.last_name},\n\nPara redefinir sua senha no GEO - EE utilize o código abaixo:\n{token}",
            from_email=None,  # usa o DEFAULT_FROM_EMAIL do settings
            recipient_list=[user.email],
            fail_silently=False,
        )
        print(f"E-mail de redefinição enviado para {user.email}")


class ResetarSenhaCompletoModelSerializer(serializers.Serializer):
    email = serializers.EmailField()
    token = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        token = data.get("token")

        try:
            user = User.objects.get(email=email)

            # Valida o token
            if not default_token_generator.check_token(user, token):
                raise serializers.ValidationError("Token inválido ou expirado.")

            self.user = user  # Armazena o usuário validado
        except User.DoesNotExist:
            raise serializers.ValidationError("E-mail não encontrado.")

        return data

    def validate_password(self, value):
        # Aqui, você pode adicionar qualquer validação extra para a senha
        return value

    def save(self):
        # Atualiza a senha do usuário
        user = self.user
        user.set_password(self.validated_data["password"])
        user.save()
        return user
