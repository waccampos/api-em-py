# Generated by Django 4.2.2 on 2023-06-27 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_rename_id_produto_registrovendas_id_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folhaponto',
            name='data_entrada',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='folhaponto',
            name='data_saida',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
