from django.db import models
from users.models import CustomUser
from shareds.models import Endereco
from django.utils.translation import gettext_lazy as _
import os
from django.conf import settings


class Empresa(models.Model):
    responsavel = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Responsável"),
    )
    nome_empresa = models.CharField(_("Nome da Empresa"), max_length=255)
    email_corporativo = models.EmailField(_("Email Corporativo"), max_length=255)
    site_empresa = models.URLField(_("Site da Empresa"), null=True, blank=True)
    linkedin_empresa = models.URLField(_("LinkedIn da Empresa"), null=True, blank=True)
    instagram_empresa = models.URLField(
        _("Instagram da Empresa"), null=True, blank=True
    )
    numero_funcionarios = models.IntegerField(
        _("Número de Funcionários"), blank=True, null=True
    )
    segmento_empresa = models.CharField(_("Segmento da Empresa"), max_length=255)
    cnpj = models.CharField(_("CNPJ"), max_length=14, unique=True)
    logo = models.ImageField(_("Logo"), upload_to="logos/", null=True, blank=True)
    banner = models.ImageField(_("Banner"), upload_to="banners/", null=True, blank=True)
    informacoes_empresa = models.TextField(
        _("Informações da Empresa"), null=True, blank=True
    )
    endereco = models.ForeignKey(
        Endereco, on_delete=models.SET_NULL, null=True, verbose_name=_("Endereço")
    )

    def __str__(self):
        return self.nome_empresa

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")

    # Sobrescrever o método delete para garantir a deleção dos arquivos logo e banner
    def delete(self, *args, **kwargs):
        # Guarda os caminhos dos arquivos antes de deletar o registro
        logo_storage = self.logo.storage
        banner_storage = self.banner.storage
        logo_path = self.logo.path if self.logo else None
        banner_path = self.banner.path if self.banner else None

        # Deleta o registro
        super().delete(*args, **kwargs)

        # Deleta os arquivos físicos se existirem
        if logo_path and logo_storage.exists(logo_path):
            logo_storage.delete(logo_path)
        if banner_path and banner_storage.exists(banner_path):
            banner_storage.delete(banner_path)
