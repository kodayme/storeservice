# Generated by Django 4.2.1 on 2023-09-28 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linea_pedido',
            old_name='pedido_id',
            new_name='pedido',
        ),
        migrations.RenameField(
            model_name='linea_pedido',
            old_name='producto_id',
            new_name='producto',
        ),
    ]
