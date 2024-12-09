from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import URLValidator


class DadosCandidato(models.Model):
    GENERO_CHOICES = (
        ("masculino", _("Masculino")),
        ("feminino", _("Feminino")),
        ("nao_respondido", _("Prefiro não responder")),
    )

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="dados_candidato",
        unique=True,
    )
    genero = models.CharField(_("Gênero"), max_length=25, choices=GENERO_CHOICES)
    deficiencia = models.BooleanField(_("Possui Deficiência"), default=False)
    tipo_deficiencia = models.CharField(
        _("Tipo de Deficiência"), max_length=255, null=True, blank=True
    )
    linkedin = models.URLField(_("LinkedIn"), blank=True, validators=[URLValidator()])
    github = models.URLField(_("GitHub"), blank=True, validators=[URLValidator()])

    def __str__(self):
        return self.usuario.get_full_name()

    class Meta:
        verbose_name = _("Dados do Candidato")
        verbose_name_plural = _("Dados dos Candidatos")


class ExperienciaAcademica(models.Model):
    STATUS_CHOICES = (
        ("Completo", _("Completo")),
        ("Incompleto", _("Incompleto")),
        ("Interrompido", _("Interrompido")),
        ("em_andamento", _("Em andamento")),
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiencias_academicas",
    )
    formacao = models.CharField(_("Formação"), max_length=100)
    curso = models.CharField(_("Curso"), max_length=255)
    status = models.CharField(
        _("Status"), max_length=20, choices=STATUS_CHOICES, default="em_andamento"
    )
    instituicao = models.CharField(_("Instituição"), max_length=255)
    inicio = models.DateField(_("Data de Início"))
    fim = models.DateField(_("Data de Conclusão"), blank=True, null=True)

    def __str__(self):
        return f"{self.formacao} - {self.curso} ({self.usuario.get_full_name()})"

    class Meta:
        verbose_name = _("Experiência Acadêmica")
        verbose_name_plural = _("Experiências Acadêmicas")


class ExperienciaProfissional(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="experiencias_profissionais",
    )
    empresa = models.CharField(_("Empresa"), max_length=255)
    cargo = models.CharField(_("Cargo"), max_length=255)
    atual = models.BooleanField(_("Emprego Atual"), default=False)
    inicio = models.DateField(_("Data de Início"))
    fim = models.DateField(_("Data de Fim"), blank=True, null=True)
    descricao_atividades = models.TextField(_("Descrição das Atividades"))

    def __str__(self):
        return f"{self.cargo} - {self.empresa} ({self.usuario.get_full_name()})"

    class Meta:
        verbose_name = _("Experiência Profissional")
        verbose_name_plural = _("Experiências Profissionais")


class Idioma(models.Model):
    NIVEL_CHOICES = (
        ("basico", _("Básico")),
        ("intermediario", _("Intermediário")),
        ("avancado", _("Avançado")),
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="idiomas",
    )
    idioma = models.CharField(_("Idioma"), max_length=50)
    nivel = models.CharField(_("Nível"), max_length=20, choices=NIVEL_CHOICES)

    def __str__(self):
        return f"{self.idioma} ({self.nivel}) - {self.usuario.get_full_name()}"

    class Meta:
        verbose_name = _("Idioma")
        verbose_name_plural = _("Idiomas")
        unique_together = ("usuario", "idioma")


class Habilidade(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="habilidades",
    )
    nome = models.CharField(_("Habilidade"), max_length=40)

    def __str__(self):
        return f"{self.nome} ({self.usuario.get_full_name()})"

    class Meta:
        verbose_name = _("Habilidade")
        verbose_name_plural = _("Habilidades")
        unique_together = ("usuario", "nome")


class Conquista(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="conquistas",
    )
    titulo = models.CharField(_("Título da Conquista"), max_length=255)
    descricao = models.TextField(_("Descrição"), blank=True)

    def __str__(self):
        return f"{self.titulo} ({self.usuario.get_full_name()})"

    class Meta:
        verbose_name = _("Conquista")
        verbose_name_plural = _("Conquistas")


class Curriculo(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="curriculos",
    )
    titulo_curriculo = models.CharField(
        _("Título Currículo"), max_length=255, null=True, blank=True
    )
    arquivo = models.FileField(_("Currículo"), upload_to="curriculos/")
    data_envio = models.DateTimeField(_("Data de Envio"), auto_now_add=True)

    def __str__(self):
        return f"Currículo de {self.usuario.get_full_name()} - Enviado em {self.data_envio.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = _("Currículo")
        verbose_name_plural = _("Currículos")

    # Sobrescrever o método delete somente para essa classe, afim de garantir a deleção dos arquivos
    def delete(self, *args, **kwargs):
        # Guarda o caminho do arquivo antes de deletar o registro
        storage = self.arquivo.storage
        path = self.arquivo.path

        # Delete o registro
        super().delete(*args, **kwargs)

        # Delete o arquivo físico
        if storage.exists(path):
            storage.delete(path)
