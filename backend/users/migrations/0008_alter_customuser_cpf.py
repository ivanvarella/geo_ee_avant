# Generated by Django 5.1.2 on 2024-11-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
    ]