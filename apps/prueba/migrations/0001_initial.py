# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('facultad', models.CharField(max_length=50, verbose_name=b'Facultad')),
                ('delegado', models.CharField(max_length=50, verbose_name=b'Delegado')),
                ('num_jugadores', models.PositiveIntegerField(default=0, verbose_name=b'Numero de Jugadores')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidads',
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=50, verbose_name=b'Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name=b'Apelldios')),
                ('fecha_nacimiento', models.DateField()),
                ('equipo', models.ForeignKey(to='prueba.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name=b'Apellido')),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50, verbose_name=b'Telefono')),
                ('especialidad', models.ForeignKey(to='prueba.Especialidad')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
    ]
