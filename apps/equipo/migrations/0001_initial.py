# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComandoTecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'ComandoTecnico',
                'verbose_name_plural': 'ComandoTecnicos',
            },
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre de Equipo')),
                ('color_camiseta', models.CharField(max_length=50, verbose_name=b'Color de Camiseta')),
                ('logo', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
            },
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70, verbose_name=b'Nombre')),
                ('siglas', models.CharField(max_length=5, verbose_name=b'Siglas')),
            ],
            options={
                'verbose_name': 'Facultad',
                'verbose_name_plural': 'Facultads',
            },
        ),
        migrations.CreateModel(
            name='JuntaDirectiva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'JuntaDirectiva',
                'verbose_name_plural': 'JuntaDirectivas',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('junta_directiva', models.ForeignKey(to='equipo.JuntaDirectiva')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
    ]
