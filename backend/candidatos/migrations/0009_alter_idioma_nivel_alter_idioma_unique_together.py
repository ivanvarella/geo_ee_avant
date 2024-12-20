# Generated by Django 5.1.2 on 2024-11-05 18:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0008_alter_experienciaacademica_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='nivel',
            field=models.CharField(choices=[('basico', 'Básico'), ('intermediario', 'Intermediário'), ('avançado', 'Avançado')], max_length=20, verbose_name='Nível'),
        ),
        migrations.AlterUniqueTogether(
            name='idioma',
            unique_together={('usuario', 'idioma')},
        ),
    ]
