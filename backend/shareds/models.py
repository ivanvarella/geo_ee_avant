from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Endereco(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enderecos"
    )
    cep = models.CharField(_("CEP"), max_length=9)
    logradouro = models.CharField(_("Logradouro"), max_length=255)
    bairro = models.CharField(_("Bairro"), max_length=100)
    # Localidade -> Cidade
    localidade = models.CharField(_("Localidade"), max_length=100)
    uf = models.CharField(_("UF"), max_length=2)
    estado = models.CharField(_("Estado"), max_length=50)
    regiao = models.CharField(_("Região"), max_length=50)

    # Campos adicionados pelo usuário - Sem API
    numero = models.CharField(_("Número"), max_length=10)
    complemento = models.CharField(_("Complemento"), max_length=100, blank=True)

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro}, {self.localidade}/{self.uf}"

    class Meta:
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")


class Telefone(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="telefones"
    )
    TIPO_CHOICES = (
        ("celular", _("Celular")),
        ("residencial", _("Residencial")),
        ("comercial", _("Comercial")),
    )
    numero = models.CharField(_("Número de telefone"), max_length=15)
    tipo = models.CharField(_("Tipo"), max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.numero}"

    class Meta:
        verbose_name = _("Telefone")
        verbose_name_plural = _("Telefones")


class CepSourceApi(models.Model):
    cep = models.CharField(_("CEP"), max_length=9)  # Campo obrigatório, mas não único
    logradouro = models.TextField(_("Logradouro"), blank=True, null=True)
    bairro = models.TextField(_("Bairro"), blank=True, null=True)
    localidade = models.TextField(_("Cidade"), blank=True, null=True)
    uf = models.CharField(_("UF"), max_length=2, blank=True, null=True)
    estado = models.CharField(_("Estado"), max_length=50, blank=True, null=True)
    regiao = models.CharField(_("Região"), max_length=50, blank=True, null=True)
    ibge = models.CharField(_("Código IBGE"), max_length=7, blank=True, null=True)
    gia = models.TextField(_("GIA"), blank=True, null=True)  # Novo campo
    ddd = models.CharField(_("DDD"), max_length=3, blank=True, null=True)
    siafi = models.CharField(_("Código SIAFI"), max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(
        _("Criado em"), auto_now_add=True, blank=True, null=True
    )

    def __str__(self):
        return (
            f"{self.logradouro}, {self.bairro}, {self.localidade}/{self.uf}"
            if self.logradouro and self.bairro and self.localidade
            else self.cep
        )

    class Meta:
        verbose_name = _("CEP")
        verbose_name_plural = _("CEPs")
