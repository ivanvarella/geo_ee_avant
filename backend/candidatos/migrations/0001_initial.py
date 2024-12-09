# Generated by Django 5.1.2 on 2024-10-17 15:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conquista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Título da Conquista')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Conquista',
                'verbose_name_plural': 'Conquistas',
            },
        ),
        migrations.CreateModel(
            name='DadosCandidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('nao_respondido', 'Prefiro não responder')], max_length=25, verbose_name='Gênero')),
                ('deficiencia', models.BooleanField(default=False, verbose_name='Possui Deficiência')),
                ('tipo_deficiencia', models.CharField(blank=True, max_length=255, verbose_name='Tipo de Deficiência')),
                ('linkedin', models.URLField(blank=True, validators=[django.core.validators.URLValidator()], verbose_name='LinkedIn')),
                ('github', models.URLField(blank=True, validators=[django.core.validators.URLValidator()], verbose_name='GitHub')),
            ],
            options={
                'verbose_name': 'Dados do Candidato',
                'verbose_name_plural': 'Dados dos Candidatos',
            },
        ),
        migrations.CreateModel(
            name='ExperienciaAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formacao', models.CharField(max_length=100, verbose_name='Formação')),
                ('curso', models.CharField(max_length=255, verbose_name='Curso')),
                ('status', models.CharField(choices=[('Completo', 'Completo'), ('Incompleto', 'Incompleto'), ('Interrompido', 'Interrompido'), ('Em andamento', 'Em andamento')], default='Em andamento', max_length=20, verbose_name='Status')),
                ('instituicao', models.CharField(max_length=255, verbose_name='Instituição')),
                ('inicio', models.DateField(verbose_name='Data de Início')),
                ('fim', models.DateField(blank=True, null=True, verbose_name='Data de Conclusão')),
            ],
            options={
                'verbose_name': 'Experiência Acadêmica',
                'verbose_name_plural': 'Experiências Acadêmicas',
            },
        ),
        migrations.CreateModel(
            name='ExperienciaProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=255, verbose_name='Empresa')),
                ('cargo', models.CharField(max_length=255, verbose_name='Cargo')),
                ('atual', models.BooleanField(default=False, verbose_name='Emprego Atual')),
                ('inicio', models.DateField(verbose_name='Data de Início')),
                ('fim', models.DateField(blank=True, null=True, verbose_name='Data de Fim')),
                ('descricao_atividades', models.TextField(verbose_name='Descrição das Atividades')),
            ],
            options={
                'verbose_name': 'Experiência Profissional',
                'verbose_name_plural': 'Experiências Profissionais',
            },
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Habilidade')),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=50, verbose_name='Idioma')),
                ('nivel', models.CharField(choices=[('Básico', 'Básico'), ('Intermediário', 'Intermediário'), ('Avançado', 'Avançado'), ('Fluente', 'Fluente')], max_length=20, verbose_name='Nível')),
            ],
            options={
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
            },
        ),
    ]