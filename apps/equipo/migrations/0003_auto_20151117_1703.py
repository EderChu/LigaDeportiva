# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20151117_1703'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='juntadirectiva',
            name='presidente',
            field=models.OneToOneField(to='torneo.Persona'),
        ),
        migrations.AddField(
            model_name='juntadirectiva',
            name='secretario',
            field=models.OneToOneField(related_name='Persona_secretario', to='torneo.Persona'),
        ),
        migrations.AddField(
            model_name='juntadirectiva',
            name='tesorero',
            field=models.OneToOneField(related_name='Persona_tesorero', to='torneo.Persona'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='comando_tecnico',
            field=models.ForeignKey(to='equipo.ComandoTecnico'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='facultad',
            field=models.ForeignKey(to='equipo.Facultad'),
        ),
        migrations.AddField(
            model_name='equipo',
            name='junta_directiva',
            field=models.ForeignKey(to='equipo.JuntaDirectiva'),
        ),
        migrations.AddField(
            model_name='comandotecnico',
            name='delegado',
            field=models.OneToOneField(related_name='Persona_delegado', to='torneo.Persona'),
        ),
        migrations.AddField(
            model_name='comandotecnico',
            name='medico',
            field=models.OneToOneField(related_name='Persona_medico', to='torneo.Persona'),
        ),
        migrations.AddField(
            model_name='comandotecnico',
            name='preparador',
            field=models.OneToOneField(related_name='Persona_preparador', to='torneo.Persona'),
        ),
        migrations.AddField(
            model_name='comandotecnico',
            name='tecnico',
            field=models.OneToOneField(to='torneo.Persona'),
        ),
    ]
