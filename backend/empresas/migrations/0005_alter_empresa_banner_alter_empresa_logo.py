# Generated by Django 5.1.2 on 2024-10-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0004_remove_empresa_representante_empresa_responsavel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banners/', verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logos/', verbose_name='Logo'),
        ),
    ]