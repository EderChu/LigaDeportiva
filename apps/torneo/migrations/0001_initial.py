# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arbitro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experiencia', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Arbitro',
                'verbose_name_plural': 'Arbitros',
            },
        ),
        migrations.CreateModel(
            name='CampoDeportivo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name=b'Direccion')),
                ('propietario', models.CharField(max_length=50, verbose_name=b'Propietario')),
                ('capacidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=50, verbose_name=b'Descripcion')),
            ],
            options={
                'verbose_name': 'CampoDeportivo',
                'verbose_name_plural': 'CampoDeportivos',
            },
        ),
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('hora', models.TimeField()),
                ('arbitro', models.ForeignKey(to='torneo.Arbitro')),
                ('campodeportiv', models.ForeignKey(to='torneo.CampoDeportivo')),
                ('elocal', models.ForeignKey(to='equipo.Equipo')),
                ('evisitante', models.ForeignKey(related_name='Equipo_evisitante', to='equipo.Equipo')),
            ],
            options={
                'verbose_name': 'Fixture',
                'verbose_name_plural': 'Fixtures',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(max_length=8, verbose_name=b'Dni')),
                ('nombres', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=50, verbose_name=b'Apellidos')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Correo Electronico')),
                ('direccion', models.CharField(max_length=50, verbose_name=b'Direccion')),
                ('sexo', models.CharField(max_length=1, verbose_name=b'sexo', choices=[(b'M', b'MASCULINO'), (b'F', b'FEMENINO')])),
                ('telefono', models.CharField(max_length=10, verbose_name=b'Telefono')),
                ('fecha_nacimineto', models.DateField(null=True, verbose_name=b'Fecha de nacimiento', blank=True)),
                ('foto', models.ImageField(upload_to=b'')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='PrecioPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=15, verbose_name=b'Concepto', choices=[(b'inscripcion', b'Inscripcion'), (b'amonestacion', b'Amonestacion'), (b'reclamo', b'Reclamo'), (b'arbitraje', b'Arbitraje')])),
                ('monto', models.DecimalField(verbose_name=b'Precio', max_digits=5, decimal_places=2)),
            ],
            options={
                'verbose_name': 'Precios',
                'verbose_name_plural': 'Precioss',
            },
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=70, verbose_name=b'Nombre')),
                ('denominacion', models.CharField(max_length=100, verbose_name=b'Denominacion')),
                ('fecha_inicio', models.DateField(verbose_name=b'Fecha Inicio')),
                ('fecha_fin', models.DateField(verbose_name=b'Fecha Fin')),
                ('bases', models.FileField(upload_to=b'', verbose_name=b'Bases')),
            ],
            options={
                'verbose_name': 'Torneo',
                'verbose_name_plural': 'Torneos',
            },
        ),
        migrations.AddField(
            model_name='fixture',
            name='torneo',
            field=models.ForeignKey(to='torneo.Torneo'),
        ),
        migrations.AddField(
            model_name='arbitro',
            name='persona',
            field=models.OneToOneField(to='torneo.Persona'),
        ),
    ]
