from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from empresas.models import Empresa
from users.models import CustomUser


class Vaga(models.Model):
    MODALIDADE_CHOICES = [
        ("PRESENCIAL", _("Presencial")),
        ("REMOTO", _("Remoto")),
        ("HIBRIDO", _("Híbrido")),
    ]

    STATUS_CHOICES = [
        ("CRIADA", _("Criada")),
        ("PUBLICADA", _("Publicada")),
        ("ENCERRADA", _("Encerrada")),
    ]

    PCD_CHOICES = [
        ("SOMENTE_PCD", _("Somente PCD")),
        ("NAO_PCD", _("Somente não PCD")),
        ("QUALQUER", _("Qualquer")),
    ]

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="vagas",
        verbose_name=_("Empresa"),
    )
    nome = models.CharField(_("Nome da Vaga"), max_length=200)
    descricao = models.TextField(_("Descrição da Vaga"))
    responsabilidades_atribuicoes = models.TextField(
        _("Responsabilidades e atribuições")
    )
    requisitos_qualificacoes = models.TextField(_("Requisitos e qualificações"))
    informacoes_adicionais = models.TextField(
        _("Informações adicionais"), blank=True, null=True
    )
    sobre_empresa = models.TextField(_("Sobre a Empresa"))
    data_publicacao = models.DateTimeField(
        _("Data de Publicação"), default=timezone.now
    )
    data_encerramento = models.DateTimeField(
        _("Data de Encerramento"), blank=True, null=True
    )
    status = models.CharField(
        _("Status"), max_length=10, choices=STATUS_CHOICES, default="CRIADA"
    )
    modalidade = models.CharField(
        _("Modalidade"), max_length=10, choices=MODALIDADE_CHOICES
    )
    pcd = models.CharField(_("PCD"), max_length=15, choices=PCD_CHOICES)
    remuneracao = models.DecimalField(
        _("Remuneração"), max_digits=10, decimal_places=2, blank=True, null=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _("Vaga")
        verbose_name_plural = _("Vagas")


class Candidatura(models.Model):
    STATUS_CHOICES = [
        ("PENDENTE", _("Pendente")),  # Default na criação
        ("APROVADO", _("Aprovado")),  # Pela empresa
        ("REJEITADO", _("Rejeitado")),  # Pela empresa
        ("CANCELADO", _("Cancelado")),  # Pelo candidato -> Desistiu de concorrer à vaga
    ]

    usuario = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="candidaturas",
        verbose_name=_("Usuário"),
    )
    vaga = models.ForeignKey(
        Vaga,
        on_delete=models.CASCADE,
        related_name="candidaturas",
        verbose_name=_("Vaga"),
    )
    data_candidatura = models.DateTimeField(
        _("Data de Candidatura"), default=timezone.now
    )
    status = models.CharField(
        _("Status"), max_length=10, choices=STATUS_CHOICES, default="PENDENTE"
    )

    def __str__(self):
        return f"{self.usuario} - {self.vaga}"

    class Meta:
        verbose_name = _("Candidatura")
        verbose_name_plural = _("Candidaturas")
        unique_together = ("usuario", "vaga")  # Só pode se candidatar uma vez
