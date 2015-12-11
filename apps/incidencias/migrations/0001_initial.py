# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20151211_1930'),
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insidencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, verbose_name=b'Tipo Insidencia')),
                ('minuto', models.CharField(max_length=10, verbose_name=b'minuto de la Insidencia')),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goles_local', models.PositiveIntegerField()),
                ('goles_visita', models.PositiveIntegerField()),
                ('fixture', models.ForeignKey(to='torneo.Fixture')),
                ('insidenci', models.ForeignKey(to='incidencias.Insidencia')),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
            },
        ),
        migrations.CreateModel(
            name='Resultados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goles_favor', models.PositiveIntegerField()),
                ('goles_contra', models.PositiveIntegerField()),
                ('equipo', models.ForeignKey(to='equipo.Equipo')),
                ('partido', models.ForeignKey(to='incidencias.Partido')),
            ],
            options={
                'verbose_name': 'Resultados',
                'verbose_name_plural': 'Resultadoss',
            },
        ),
    ]
