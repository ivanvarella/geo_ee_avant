# Generated by Django 5.1.2 on 2024-10-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareds', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CepSourceApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.TextField(blank=True, null=True, verbose_name='Logradouro')),
                ('bairro', models.TextField(blank=True, null=True, verbose_name='Bairro')),
                ('localidade', models.TextField(blank=True, null=True, verbose_name='Cidade')),
                ('uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
                ('estado', models.CharField(blank=True, max_length=50, null=True, verbose_name='Estado')),
                ('regiao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Região')),
                ('ibge', models.CharField(blank=True, max_length=7, null=True, verbose_name='Código IBGE')),
                ('gia', models.TextField(blank=True, null=True, verbose_name='GIA')),
                ('ddd', models.CharField(blank=True, max_length=3, null=True, verbose_name='DDD')),
                ('siafi', models.CharField(blank=True, max_length=7, null=True, verbose_name='Código SIAFI')),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'CEP',
                'verbose_name_plural': 'CEPs',
            },
        ),
    ]