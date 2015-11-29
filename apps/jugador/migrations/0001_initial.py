# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20151129_0505'),
        ('torneo', '0001_initial'),
        ('incidencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amonestacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_amonestacion', models.CharField(max_length=1, verbose_name=b'Tipo de Amonestacion', choices=[(b'A', b'Amarilla'), (b'R', b'Roja'), (b'T', b'Tecnica')])),
                ('condicion', models.CharField(max_length=1, verbose_name=b'Condicion', choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('peso_amonestacion', models.PositiveIntegerField()),
                ('descripcion', models.TextField()),
            ],
            options={
                'verbose_name': 'Amonestacion',
                'verbose_name_plural': 'Amonestacions',
            },
        ),
        migrations.CreateModel(
            name='Goleadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_goles', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'goles',
                'verbose_name_plural': 'goless',
            },
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posicion', models.CharField(max_length=50, verbose_name=b'Posicion')),
                ('numero_camiseta', models.PositiveIntegerField(verbose_name=b'Numero de Camiseta')),
                ('estado', models.BooleanField(verbose_name=b'Habilitado')),
                ('equipo', models.ForeignKey(to='equipo.Equipo')),
                ('persona', models.OneToOneField(to='torneo.Persona')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadors',
            },
        ),
        migrations.AddField(
            model_name='goleadores',
            name='jugador',
            field=models.ForeignKey(to='jugador.Jugador'),
        ),
        migrations.AddField(
            model_name='goleadores',
            name='partido',
            field=models.ForeignKey(to='incidencias.Partido'),
        ),
        migrations.AddField(
            model_name='amonestacion',
            name='jugador',
            field=models.ForeignKey(to='jugador.Jugador'),
        ),
        migrations.AddField(
            model_name='amonestacion',
            name='partido',
            field=models.ForeignKey(to='incidencias.Partido'),
        ),
    ]
