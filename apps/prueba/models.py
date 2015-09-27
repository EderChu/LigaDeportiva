from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    facultad = models.CharField('Ciudad', max_length=50)
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



    