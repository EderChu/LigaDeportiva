# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    facultad = models.CharField('Facultad', max_length=50)
    delegado = models.CharField('Delegado', max_length=50)
    num_jugadores = models.PositiveIntegerField('Numero de Jugadores',default=0)

    def __unicode__(self):
        return self.nombre

class Jugador(models.Model):
    nombres = models.CharField('Nombres', max_length=50)
    apellidos = models.CharField('Apelldios', max_length=50)
    fecha_nacimiento = models.DateField()
    equipo = models.ForeignKey(Equipo)

    def __unicode__(self):
        return self.nombres



class Especialidad(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidads"

    def __unicode__(self):
        return self.nombre
    

class Medico(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellido', max_length=50)
    email = models.EmailField()
    telefono = models.CharField('Telefono', max_length=50)
    especialidad = models.ForeignKey(Especialidad)
    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __unicode__(self):
        return self.nombre


class Policia(models.Model):
    POLICE_CHOICES = (
        ('1', 'SOLDAO'),
        ('2', 'CAPITAN'),
        ('3', 'GENERAL'),
    )
    full_name = models.CharField('Nombres', max_length=50)
    email = models.EmailField()
    sueldo = models.DecimalField('Sueldo', max_digits=5, decimal_places=2)
    rango = models.CharField('Rango', max_length=1, choices=POLICE_CHOICES)

    class Meta:
        verbose_name = "Policia"
        verbose_name_plural = "Policias"

    def __unicode__(self):
        return self.full_name
    
    



    