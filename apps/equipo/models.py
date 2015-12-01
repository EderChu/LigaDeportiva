# -*- encoding: utf-8 -*-
from django.db import models
from apps.users.models import User
from apps.torneo.models import Persona, PrecioPago, Torneo
# Create your models here.


class JuntaDirectiva(models.Model):
    presidente = models.OneToOneField(User)
    secretario = models.OneToOneField(
        Persona,
        related_name="Persona_secretario",
        blank=True,
        null=True,
    )
    tesorero = models.OneToOneField(
        Persona,
        related_name="Persona_tesorero",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "JuntaDirectiva"
        verbose_name_plural = "JuntaDirectivas"

    def __unicode__(self):
        return "%s" % str(self.presidente)


class ComandoTecnico(models.Model):
    junta_directiva = models.OneToOneField(JuntaDirectiva)
    tecnico = models.OneToOneField(
        Persona,
        blank=True,
        null=True,
    )
    medico = models.OneToOneField(
        Persona,
        related_name="Persona_medico",
        blank=True,
        null=True,
    )
    preparador = models.OneToOneField(
        Persona,
        related_name="Persona_preparador",
        blank=True,
        null=True,
    )
    delegado = models.OneToOneField(
        Persona,
        related_name="Persona_delegado",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "ComandoTecnico"
        verbose_name_plural = "ComandoTecnicos"

    def __unicode__(self):
        return "%s" % str(self.tecnico)


class Facultad(models.Model):
    nombre = models.CharField(
        'Nombre',
        max_length=70
    )
    siglas = models.CharField(
        'Siglas',
        max_length=5)

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultads"

    def __unicode__(self):
        return self.nombre


class Pago(models.Model):
    precio_pago = models.ForeignKey(PrecioPago)
    junta_directiva = models.ForeignKey(JuntaDirectiva)
    torneo = models.ForeignKey(Torneo)
    fecha = models.DateField()
    usuario = models.ForeignKey(User)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __unicode__(self):
        return "%s" % str(self.junta_directiva)


class Equipo(models.Model):
    nombre = models.CharField(
        'Nombre de Equipo',
        max_length=50,
        blank=True,
        null=True,
    )
    color_camiseta = models.CharField(
        'Color de Camiseta',
        max_length=50,
        blank=True,
        null=True,
    )
    junta_directiva = models.ForeignKey(JuntaDirectiva)
    comando_tecnico = models.ForeignKey(
        ComandoTecnico,
        blank=True,
        null=True,
    )
    facultad = models.ForeignKey(Facultad)
    logo = models.IntegerField(blank=True, null=True)
    estado = models.BooleanField(
        'Habilitado',
        default=False,
    )

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __unicode__(self):
        return "%s" % str(self.facultad)
