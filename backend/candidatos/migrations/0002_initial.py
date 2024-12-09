# Generated by Django 5.1.2 on 2024-10-17 15:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidatos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='conquista',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conquistas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dadoscandidato',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dados_candidato', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experienciaacademica',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencias_academicas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experienciaprofissional',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencias_profissionais', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='habilidade',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilidades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='idioma',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idiomas', to=settings.AUTH_USER_MODEL),
        ),
    ]