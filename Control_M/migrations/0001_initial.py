# Generated by Django 3.2.7 on 2021-09-24 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Control_Em', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico_Especialista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
            ],
            options={
                'db_table': 'Medico_Especialista',
            },
        ),
        migrations.CreateModel(
            name='Empadre_medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empadre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control_Em.control_empadre')),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Control_M.medico_especialista')),
            ],
            options={
                'db_table': 'Empadre_Medico',
            },
        ),
    ]
