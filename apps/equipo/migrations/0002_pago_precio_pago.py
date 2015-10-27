# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='precio_pago',
            field=models.ForeignKey(to='torneo.PrecioPago'),
        ),
    ]
