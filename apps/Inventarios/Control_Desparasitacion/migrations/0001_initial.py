# Generated by Django 3.2.7 on 2021-11-24 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Control_IMedicos', '0001_initial'),
        ('Control_Ganado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Control_Desparasitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_desparacitacion', models.CharField(max_length=250)),
                ('id_ganado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control_Ganado.ganado')),
                ('id_medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control_IMedicos.inventario_insumos')),
            ],
        ),
    ]