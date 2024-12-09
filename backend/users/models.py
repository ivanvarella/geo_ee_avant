from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# Alterar a forma de criar superuser - default tipo = "administrador"
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e retorna um usuário com o email e senha fornecidos.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Cria e retorna um superusuário com o tipo 'administrador'.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("tipo", "administrador")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuários devem ter is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuários devem ter is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ("administrador", _("Administrador")),
        ("funcionario", _("Funcionário")),
        ("candidato", _("Candidato")),
        ("responsavel", _("Responsável de Empresa")),
    ]
    tipo = models.CharField(
        _("Tipo de Usuário"),
        max_length=15,
        choices=TIPO_USUARIO_CHOICES,
        default="candidato",
    )
    email = models.EmailField(_("Email address"), unique=True)  # unique
    is_email_verified = models.BooleanField(default=False)
    cpf = models.CharField(_("CPF"), max_length=14, unique=True, null=True, blank=False)
    data_nascimento = models.DateField(_("Data de Nascimento"), null=True, blank=True)
    username = models.CharField(
        _("username"),
        max_length=50,
        null=True,
        blank=True,
        unique=False,
        default="",
    )

    USERNAME_FIELD = "email"  # Email as the primary identifier
    REQUIRED_FIELDS = ["username"]  # Remains mandatory

    objects = CustomUserManager()  # Associa o CustomUserManager aqui

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Como o username não é mais mandatório, mostra o email
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("Usuário")
        verbose_name_plural = _("Usuários")

    # Para resolver o problema de criação do superuser
    def save(self, *args, **kwargs):
        # Preenche automaticamente o campo 'username' com o valor de 'email' se não estiver preenchido
        if not self.username:
            self.username = self.email
        super().save(*args, **kwargs)
