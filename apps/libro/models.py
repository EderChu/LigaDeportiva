# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.
#clase para uator
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autors"

    def __unicode__(self):
        return self.nombre


#calse editorial
class Editorial(models.Model):
    denominacion = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Editorial"
        verbose_name_plural = "Editorials"

    def __unicode__(self):
        return self.denominacion


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    edicion = models.CharField(max_length=50)
    autor = models.ForeignKey(Autor)
    editorial = models.ForeignKey(Editorial)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __unicode__(self):
        return self.titulo