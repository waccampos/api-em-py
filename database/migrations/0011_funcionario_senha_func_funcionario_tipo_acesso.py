# Generated by Django 4.2.2 on 2023-06-27 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_alter_registrovendas_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='senha_func',
            field=models.CharField(default='12345', max_length=30),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='tipo_acesso',
            field=models.TextField(default='padrao'),
        ),
    ]
