# Generated by Django 5.1.2 on 2024-10-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('localidade', models.CharField(max_length=100, verbose_name='Localidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado')),
                ('regiao', models.CharField(max_length=50, verbose_name='Região')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15, verbose_name='Número de telefone')),
                ('tipo', models.CharField(choices=[('celular', 'Celular'), ('residencial', 'Residencial'), ('comercial', 'Comercial')], max_length=20, verbose_name='Tipo')),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
    ]
