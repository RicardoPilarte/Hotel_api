# Generated by Django 4.0 on 2024-07-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('telefono', models.CharField(max_length=8)),
                ('email', models.CharField(max_length=50, null=True)),
                ('tipo_identificacion', models.CharField(choices=[('Cedula', 'CEDULA'), ('Pasaporte', 'PASAPORTE')], max_length=9)),
                ('num_identificacion', models.CharField(default='000-000000-0000A', max_length=30)),
                ('eliminado', models.CharField(default='NO', max_length=2)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Cliente',
            },
        ),
    ]