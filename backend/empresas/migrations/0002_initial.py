# Generated by Django 5.1.2 on 2024-10-17 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        ('shareds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='endereco',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shareds.endereco', verbose_name='Endereço'),
        ),
    ]
