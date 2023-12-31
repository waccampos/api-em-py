# Generated by Django 4.2.2 on 2023-06-28 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_rename_pratileira_estoque_prateleira'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='id_produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.produto'),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='prateleira',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='setor',
            field=models.TextField(),
        ),
    ]
