# -*- encoding: utf-8 -*-
from django.db import models
from apps.torneo.models import Persona
from apps.incidencias.models import Partido
from apps.equipo.models import Equipo

# Create your models here.


class Jugador(models.Model):
    persona = models.OneToOneField(Persona)
    equipo = models.ForeignKey(Equipo)
    posicion = models.CharField('Posicion', max_length=50)
    numero_camiseta = models.PositiveIntegerField('Numero de Camiseta')
    estado = models.BooleanField('Habilitado')

    class Meta:
        verbose_name = "Jugador"
        verbose_name_plural = "Jugadors"

    def __unicode__(self):
        return self.persona


class Amonestacion(models.Model):
    TIPO_CHOICES = (
        ('A', 'Amarilla'),
        ('R', 'Roja'),
        ('T', 'Tecnica'),
    )

    CONDICION_CHOICES = (
        ('A', 'Activo'),
        ('I', 'Inactivo'),
    )

    jugador = models.ForeignKey(Jugador)
    tipo_amonestacion = models.CharField(
        'Tipo de Amonestacion',
        max_length=1,
        choices=TIPO_CHOICES
    )
    condicion = models.CharField(
        'Condicion',
        max_length=1,
        choices=CONDICION_CHOICES
    )
    partido = models.ForeignKey(Partido)
    peso_amonestacion = models.PositiveIntegerField()
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Amonestacion"
        verbose_name_plural = "Amonestacions"

    def __unicode__(self):
        return jugador


class Goleadores(models.Model):
    jugador = models.ForeignKey(Jugador)
    partido = models.ForeignKey(Partido)
    num_goles = models.PositiveIntegerField()

    class Meta:
        verbose_name = "goles"
        verbose_name_plural = "goless"

    def __unicode__(self):
        return self.jugador
