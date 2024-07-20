# Generated by Django 4.0 on 2024-07-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alojamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('tiempo_estadia', models.PositiveIntegerField(default=0)),
                ('eliminado', models.CharField(default='NO', max_length=2)),
            ],
            options={
                'verbose_name': 'Alojamiento',
                'verbose_name_plural': 'Alojamientos',
                'db_table': 'Alojamiento',
            },
        ),
    ]
