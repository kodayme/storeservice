# Generated by Django 4.2.1 on 2023-08-31 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcontenido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenido',
            name='categoria',
        ),
        migrations.AddField(
            model_name='contenido',
            name='categoria',
            field=models.ManyToManyField(to='appcontenido.categoria'),
        ),
    ]
