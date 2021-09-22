# Generated by Django 3.2.7 on 2021-09-17 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Raza',
            },
        ),
        migrations.CreateModel(
            name='Ganado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('sexo', models.CharField(max_length=254)),
                ('num_economico', models.CharField(max_length=254)),
                ('num_registro', models.CharField(max_length=254)),
                ('num_siniga', models.CharField(max_length=254)),
                ('comentarios', models.CharField(max_length=254)),
                ('dia_nacimiento', models.IntegerField(max_length=100)),
                ('mes_nacimiento', models.IntegerField(max_length=100)),
                ('anio_nacimiento', models.IntegerField(max_length=100)),
                ('padre', models.CharField(max_length=254)),
                ('madre', models.CharField(max_length=254)),
                ('dia_entrada_hato', models.IntegerField(max_length=100)),
                ('mes_entrada_hato', models.IntegerField(max_length=100)),
                ('anio_entrada_hato', models.IntegerField(max_length=100)),
                ('estado', models.CharField(max_length=254)),
                ('condicion_estadia', models.CharField(max_length=254)),
                ('id_raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control_G.raza')),
            ],
            options={
                'db_table': 'Ganado',
            },
        ),
    ]
