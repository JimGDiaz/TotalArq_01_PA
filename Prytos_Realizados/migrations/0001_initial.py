# Generated by Django 5.0.3 on 2024-05-14 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uso_Edif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=30)),
                ('sub_genero', models.CharField(max_length=36)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'uso_Edif',
                'verbose_name_plural': 'usos_Edif',
            },
        ),
        migrations.CreateModel(
            name='Prytos_Realizados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('persona_funcion', models.CharField(max_length=75)),
                ('ubicacion', models.CharField(max_length=60)),
                ('descripcion', models.TextField(max_length=300, verbose_name='Contenido:')),
                ('imagen_D', models.ImageField(upload_to='prytos_realizados_media')),
                ('imagen_A', models.ImageField(upload_to='prytos_realizados_media')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateField(auto_now_add=True)),
                ('usos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prytos_Realizados.uso_edif')),
            ],
            options={
                'verbose_name': 'pryto_realizado',
                'verbose_name_plural': 'prytos_realizados',
            },
        ),
    ]