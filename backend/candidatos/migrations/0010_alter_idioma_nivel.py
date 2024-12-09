# Generated by Django 5.1.2 on 2024-11-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0009_alter_idioma_nivel_alter_idioma_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idioma',
            name='nivel',
            field=models.CharField(choices=[('basico', 'Básico'), ('intermediario', 'Intermediário'), ('avancado', 'Avançado')], max_length=20, verbose_name='Nível'),
        ),
    ]