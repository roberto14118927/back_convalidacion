# Generated by Django 3.2.7 on 2021-09-28 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Control_G', '0002_auto_20210924_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ganado',
            name='id_raza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='id_raza', to='Control_G.raza'),
        ),
    ]