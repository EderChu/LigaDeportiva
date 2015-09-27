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
                ('facultad', models.CharField(max_length=50, verbose_name=b'Ciudad')),
                ('delegado', models.CharField(max_length=50, verbose_name=b'Delegado')),
                ('num_jugadores', models.PositiveIntegerField(default=0, verbose_name=b'Numero de Jugadores')),
            ],
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
    ]
