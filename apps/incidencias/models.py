# -*- encoding: utf-8 -*-
from django.db import models
from apps.torneo.models import Fixture
from apps.equipo.models import Equipo
from apps.users.models import User
# Create your models here.


class Insidencia(models.Model):
    tipo = models.CharField('Tipo Insidencia', max_length=50)
    minuto = models.CharField('minuto de la Insidencia', max_length=10)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User)

    def __str__(self):
        return self.tipo
    

class Partido(models.Model):
    fixture = models.ForeignKey(Fixture)
    goles_local = models.PositiveIntegerField()
    goles_visita = models.PositiveIntegerField()
    insidenci = models.ForeignKey(Insidencia)
    class Meta:
        verbose_name = "Partido"
        verbose_name_plural = "Partidos"

    def __unicode__(self):
        return self.fixture


class Resultados(models.Model):
    partido = models.ForeignKey(Partido)
    equipo = models.ForeignKey(Equipo)
    goles_favor = models.PositiveIntegerField()
    goles_contra = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Resultados"
        verbose_name_plural = "Resultadoss"

    def __unicode__(self):
        return self.equipo
    
    