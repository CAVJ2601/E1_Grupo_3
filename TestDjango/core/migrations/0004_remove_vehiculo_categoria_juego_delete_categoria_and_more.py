# Generated by Django 5.0.4 on 2024-04-12 01:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_categoriajuego_remove_vehiculo_categoria_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id_juego', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Código')),
                ('nombre_juego', models.CharField(max_length=50, verbose_name='Nombre')),
                ('descripcion_juego', models.CharField(max_length=100, verbose_name='Descripción')),
                ('url_img_juego', models.CharField(max_length=50, verbose_name='URL imagen')),
                ('precio_juego', models.IntegerField(verbose_name='Precio')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoriajuego')),
            ],
        ),

    ]
