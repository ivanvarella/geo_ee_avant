# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CandidatosConquista(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'candidatos_conquista'


class CandidatosCurriculo(models.Model):
    arquivo = models.CharField(max_length=100)
    data_envio = models.DateTimeField()
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)
    titulo_curriculo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'candidatos_curriculo'


class CandidatosDadoscandidato(models.Model):
    genero = models.CharField(max_length=25)
    deficiencia = models.BooleanField()
    tipo_deficiencia = models.CharField(max_length=255)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    usuario = models.OneToOneField('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'candidatos_dadoscandidato'


class CandidatosExperienciaacademica(models.Model):
    formacao = models.CharField(max_length=100)
    curso = models.CharField(max_length=255)
    instituicao = models.CharField(max_length=255)
    inicio = models.DateField()
    fim = models.DateField(blank=True, null=True)
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'candidatos_experienciaacademica'


class CandidatosExperienciaprofissional(models.Model):
    empresa = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    atual = models.BooleanField()
    inicio = models.DateField()
    fim = models.DateField(blank=True, null=True)
    descricao_atividades = models.TextField()
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'candidatos_experienciaprofissional'


class CandidatosHabilidade(models.Model):
    nome = models.CharField(max_length=40)
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'candidatos_habilidade'
        unique_together = (('usuario', 'nome'),)


class CandidatosIdioma(models.Model):
    idioma = models.CharField(max_length=50)
    nivel = models.CharField(max_length=20)
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'candidatos_idioma'
        unique_together = (('usuario', 'idioma'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmpresasEmpresa(models.Model):
    nome_empresa = models.CharField(max_length=255)
    email_corporativo = models.CharField(max_length=255)
    linkedin_empresa = models.CharField(max_length=200, blank=True, null=True)
    instagram_empresa = models.CharField(max_length=200, blank=True, null=True)
    numero_funcionarios = models.IntegerField(blank=True, null=True)
    segmento_empresa = models.CharField(max_length=255)
    cnpj = models.CharField(unique=True, max_length=14)
    logo = models.CharField(max_length=100, blank=True, null=True)
    banner = models.CharField(max_length=100, blank=True, null=True)
    informacoes_empresa = models.TextField(blank=True, null=True)
    endereco = models.ForeignKey('SharedsEndereco', models.DO_NOTHING, blank=True, null=True)
    responsavel = models.OneToOneField('UsersCustomuser', models.DO_NOTHING)
    site_empresa = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresas_empresa'


class SharedsCepsourceapi(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.TextField(blank=True, null=True)
    bairro = models.TextField(blank=True, null=True)
    localidade = models.TextField(blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    estado = models.CharField(max_length=50, blank=True, null=True)
    regiao = models.CharField(max_length=50, blank=True, null=True)
    ibge = models.CharField(max_length=7, blank=True, null=True)
    gia = models.TextField(blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    siafi = models.CharField(max_length=7, blank=True, null=True)
    criado_em = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shareds_cepsourceapi'


class SharedsEndereco(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    estado = models.CharField(max_length=50)
    regiao = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100)
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shareds_endereco'


class SharedsTelefone(models.Model):
    numero = models.CharField(max_length=15)
    tipo = models.CharField(max_length=20)
    usuario = models.ForeignKey('UsersCustomuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'shareds_telefone'


class TokenBlacklistBlacklistedtoken(models.Model):
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('UsersCustomuser', models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class UsersCustomuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    data_nascimento = models.DateField(blank=True, null=True)
    tipo = models.CharField(max_length=15)
    cpf = models.CharField(unique=True, max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_customuser'


class UsersCustomuserGroups(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_groups'
        unique_together = (('customuser', 'group'),)


class UsersCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class VagasCandidatura(models.Model):
    data_candidatura = models.DateTimeField()
    status = models.CharField(max_length=10)
    usuario = models.ForeignKey(UsersCustomuser, models.DO_NOTHING)
    vaga = models.ForeignKey('VagasVaga', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vagas_candidatura'
        unique_together = (('usuario', 'vaga'),)


class VagasVaga(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    responsabilidades_atribuicoes = models.TextField()
    requisitos_qualificacoes = models.TextField()
    informacoes_adicionais = models.TextField(blank=True, null=True)
    sobre_empresa = models.TextField()
    data_publicacao = models.DateTimeField()
    data_encerramento = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10)
    modalidade = models.CharField(max_length=10)
    pcd = models.CharField(max_length=15)
    remuneracao = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    empresa = models.ForeignKey(EmpresasEmpresa, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vagas_vaga'
