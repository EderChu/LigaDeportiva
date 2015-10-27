# -*- encoding: utf-8 -*-
from django.db import models
from apps.users.models import User
from apps.torneo.models import Persona, PrecioPago
# Create your models here.
class JuntaDirectiva(models.Model):
    presidente = models.OneToOneField(Persona)
    secretario = models.OneToOneField(Persona, related_name="Persona_secretario")
    tesorero = models.OneToOneField(Persona, related_name="Persona_tesorero")

    class Meta:
        verbose_name = "JuntaDirectiva"
        verbose_name_plural = "JuntaDirectivas"

    def __unicode__(self):
        return self.presidente
    
class ComandoTecnico(models.Model):
    tecnico = models.OneToOneField(Persona)
    medico = models.OneToOneField(Persona, related_name="Persona_medico")
    preparador = models.OneToOneField(Persona, related_name="Persona_preparador")
    delegado = models.OneToOneField(Persona, related_name="Persona_delegado")

    class Meta:
        verbose_name = "ComandoTecnico"
        verbose_name_plural = "ComandoTecnicos"

    def __unicode__(self):
        return self.tecnico
    

class Facultad(models.Model):
    nombre = models.CharField('Nombre', max_length=70)
    siglas = models.CharField('Siglas', max_length=5)
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultads"

    def __unicode__(self):
        return nombre
    
class Pago(models.Model):
    precio_pago = models.ForeignKey(PrecioPago)
    junta_directiva = models.ForeignKey(JuntaDirectiva)
    fecha = models.DateField()
    usuario = models.ForeignKey(User)
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __unicode__(self):
        return self.junta_directiva
    

class Equipo(models.Model):
    nombre = models.CharField('Nombre de Equipo', max_length=50)
    color_camiseta = models.CharField('Color de Camiseta', max_length=50)
    junta_directiva = models.ForeignKey(JuntaDirectiva)
    comando_tecnico = models.ForeignKey(ComandoTecnico)
    facultad = models.ForeignKey(Facultad)

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"

    def __unicode__(self):
        return self.nombre
    