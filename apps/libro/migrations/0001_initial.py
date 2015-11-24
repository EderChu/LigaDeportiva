# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autors',
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('denominacion', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Editorial',
                'verbose_name_plural': 'Editorials',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('edicion', models.CharField(max_length=50)),
                ('autor', models.ForeignKey(to='libro.Autor')),
                ('editorial', models.ForeignKey(to='libro.Editorial')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
