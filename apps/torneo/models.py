# -*- encoding: utf-8 -*-
from django.db import models
# Create your models here.


class Persona(models.Model):
    GENDER_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    )

    dni = models.CharField(
        'Dni',
        max_length=8
    )
    nombres = models.CharField(
        'Nombre',
        max_length=50
    )
    apellidos = models.CharField(
        'Apellidos',
        max_length=50
    )
    email = models.EmailField(
        'Correo Electronico'
    )
    direccion = models.CharField(
        'Direccion',
        max_length=50
    )
    sexo = models.CharField(
        'sexo',
        max_length=1,
        choices=GENDER_CHOICES
    )
    telefono = models.CharField(
        'Telefono', max_length=10)
    fecha_nacimineto = models.DateField(
        'Fecha de nacimiento',
        blank=True,
        null=True
    )
    foto = models.ImageField()

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __unicode__(self):
        return "%s %s" % (self.nombres, self.apellidos)


class Torneo(models.Model):
    nombre = models.CharField('Nombre', max_length=70)
    denominacion = models.CharField('Denominacion', max_length=100)
    fecha_inicio = models.DateField('Fecha Inicio')
    fecha_fin = models.DateField('Fecha Fin')
    bases = models.FileField('Bases')
    class Meta:
        verbose_name = "Torneo"
        verbose_name_plural = "Torneos"

    def __unicode__(self):
        return self.denominacion


class Arbitro(models.Model):
    persona = models.OneToOneField(Persona)
    experiencia = models.IntegerField()
    class Meta:
        verbose_name = "Arbitro"
        verbose_name_plural = "Arbitros"

    def __unicode__(self):
        return self.persona


class CampoDeportivo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    direccion = models.CharField('Direccion', max_length=100)
    propietario = models.CharField('Propietario', max_length=50)
    capacidad = models.IntegerField()
    descripcion = models.CharField('Descripcion', max_length=50)
    class Meta:
        verbose_name = "CampoDeportivo"
        verbose_name_plural = "CampoDeportivos"

    def __unicode__(self):
        return self.nombre


class PrecioPago(models.Model):
    CONCEPTO_CHOICES = (
        ('inscripcion', 'Inscripcion'),
        ('amonestacion', 'Amonestacion'),
        ('reclamo', 'Reclamo'),
        ('arbitraje', 'Arbitraje'),
    )

    concepto = models.CharField('Concepto', max_length=15, choices=CONCEPTO_CHOICES)
    monto = models.DecimalField('Precio', max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = "Precios"
        verbose_name_plural = "Precioss"

    def __unicode__(self):
        return self.concepto


class Fixture(models.Model):
    torneo = models.ForeignKey(Torneo)
    elocal = models.ForeignKey('equipo.Equipo')
    evisitante = models.ForeignKey('equipo.Equipo', related_name="Equipo_evisitante")
    campodeportiv = models.ForeignKey(CampoDeportivo)
    arbitro = models.ForeignKey(Arbitro)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField()

    class Meta:
        verbose_name = "Fixture"
        verbose_name_plural = "Fixtures"

    def __unicode__(self):
        return self.fecha