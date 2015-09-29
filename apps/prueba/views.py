from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy

from django.utils import timezone

from .models import Equipo, Jugador

from .forms import *

# Create your views here.
"""MANTENIMIENTOS DE TABLA EQUIPO"""
#clase para lista la lista de equipos de la base de datos
class ListEquipo(TemplateView):
    #pasamos el html donde se mostrara la lista de equipos
    template_name = 'prueba/equipo/list_equipo.html'

    #funcion para consultar y retornar la lista de equipos
    def get_context_data(self, **kwargs):
        #sobre-escribimos el context_data para devolver un contexto personaliado
        context = super(ListEquipo, self).get_context_data(**kwargs)
        #realizamos la consulta a base de datos y retornamos en un context equipos
        context['equipos'] = Equipo.objects.all().order_by('nombre')
        #devolcemos el contexto: resultado de la consulta
        return context

#clase para registrar un equipo utilizando createview
class RegistrarEquipo(CreateView):
    form_class = EquipoForm
    template_name = "prueba/equipo/agregar.html"
    success_url = reverse_lazy('users_app:inicio')

#clase para ver los datos en detalle de un solo equipo
# utilizaremos un DetaiView que se encarga de recibir el id de equipo
class DetalleEquipo(DetailView):
    # pasamos hatml donde se pintara el detalle del objeto
    template_name = 'prueba/equipo/detalle.html'
    #pasamos el modelo o tabla del objeto
    model = Equipo

#clase para modificar un registro de una tabla
#utilizamos UpdateView que se encarga de recuperar el objeto y actualizarlo
class ModificarEquipo(UpdateView):
    #le especificamos la tabla de BD
    model = Equipo
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'prueba/equipo/modificar.html'
    success_url = reverse_lazy('prueba_app:listar_equipo')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = EquipoForm

#clase para eliminar un registro de la BD
#utilizamos DeleteView que se encarga de recibir y elimnar los dato de la BD
class EliminarEquipo(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'prueba/equipo/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = Equipo
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('prueba_app:listar_equipo')



"MANTENIMIENTOS DE TABLA JUGADOR"

class ListJugador(TemplateView):
    #pasamos el html donde se mostrara la lista de jugadores
    template_name = 'prueba/jugador/list_jugador.html'

    #funcion para consultar y retornar la lista de jugadores
    def get_context_data(self, **kwargs):
        #sobre-escribimos el context_data para devolver un contexto personaliado
        context = super(ListJugador, self).get_context_data(**kwargs)
        #realizamos la consulta a base de datos y retornamos en un context juagadores
        #ordenamos por equipo
        context['jugadores'] = Jugador.objects.all().order_by('equipo')
        #devolcemos el contexto: resultado de la consulta
        return context

#clase para registrar un jugador y actuallizar numero de jugadores de equipo
class RegisterJugador(FormView):
    template_name = "prueba/jugador/agregar.html"
    form_class = JugadorForm
    success_url = reverse_lazy('prueba_app:jugador')

    def form_valid(self, form):
        #recuperamos los datos de jugador
        nom = form.cleaned_data['nombres']
        apellido = form.cleaned_data['apellidos']
        nacimiento = form.cleaned_data['fecha_nacimiento']
        #recuperamos el objeto equipo de juagor
        equipo = form.cleaned_data['equipo']

        #guardamos jugador
        jugador = Jugador(
                    nombres=nom,
                    apellidos=apellido,
                    fecha_nacimiento=nacimiento,
                    equipo=equipo        
                        )
        jugador.save()

        #actualizamos numero de jugadores en equipo
        equipo.numero_jugadores = equipo.num_jugadores + 1
        equipo.save()

        return super(RegisterJugador,self).form_valid(form)
        
        