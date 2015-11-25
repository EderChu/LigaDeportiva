# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy, reverse


from .forms import CampoDForm, PersonaForm, TorneoForm, ArbitroForm
from .models import CampoDeportivo, Persona, Torneo, Arbitro, Fixture


from django.http import HttpResponseRedirect
from django.utils import timezone


# Create your views here.
#Mantenimientos del campo deportivo
class ListarCampoD(ListView):
    context_object_name = 'campos'
    queryset = CampoDeportivo.objects.all()
    template_name = 'torneo/campodeportivo/listar.html'


class RegistrarCampoD(CreateView):
    form_class = CampoDForm
    template_name = "torneo/campodeportivo/agregar.html"
    success_url = reverse_lazy('torneo_app:listar_CampoD')


class detalleCampoD(DetailView):
    template_name = 'torneo/campodeportivo/detalle.html'
    model = CampoDeportivo


class ModificarCampoD(UpdateView):
    #le especificamos la tabla de BD
    model = CampoDeportivo
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'torneo/campodeportivo/modificar.html'
    success_url = reverse_lazy('torneo_app:listar_CampoD')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = CampoDForm


#utilizamos DeleteView que se encarga de recibir y elimnar los dato de la BD
class EliminarCampoD(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'torneo/campodeportivo/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = CampoDeportivo
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('torneo_app:listar_CampoD')


class ListPersona(ListView):
    context_object_name = 'personas'
    queryset = Persona.objects.all()
    template_name = 'torneo/persona/listar.html'


class RegistrarPersona(CreateView):
    form_class = PersonaForm
    template_name = "torneo/persona/agregar.html"
    success_url = reverse_lazy('torneo_app:listar-persona')


class DetallePersona(DetailView):
    # pasamos hatml donde se pintara el detalle del objeto
    template_name = 'torneo/persona/detalle.html'
    #pasamos el modelo o tabla del objeto
    model = Persona


class ModificarPersona(UpdateView):
    #le especificamos la tabla de BD
    model = Persona
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'torneo/persona/modificar.html'
    success_url = reverse_lazy('torneo_app:listar-persona')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = PersonaForm


class EliminarPersona(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'torneo/persona/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = Persona
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('torneo_app:listar-persona')


class ListTorneo(ListView):
    template_name = 'torneo/torneo/listar.html'
    context_object_name = 'torneos'
    model = Torneo


class RegistrarTorneo(CreateView):
    form_class = TorneoForm
    template_name = "torneo/torneo/agregar.html"
    success_url = reverse_lazy('torneo_app:listar_torneo')


class DetalleTorneo(DetailView):
    template_name = 'torneo/torneo/detalle.html'
    #pasamos el modelo o tabla del objeto
    model = Torneo


class ModificarTorneo(UpdateView):
    model = Torneo
    template_name = 'torneo/torneo/modificar.html'
    success_url = reverse_lazy('torneo_app:listar_torneo')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = TorneoForm


class EliminarTorneo(DeleteView):
    template_name = 'torneo/torneo/eliminar.html'
    model = Torneo
    success_url = reverse_lazy('torneo_app:listar_torneo')


#Mantenimientos del arbitro
class ListarArbitro(ListView):
    context_object_name = 'campos'
    queryset = Arbitro.objects.all()
    template_name = 'torneo/arbitro/listar.html'


#clase para registrar un equipo utilizando createview
class RegistrarArbitro(CreateView):
    form_class = ArbitroForm
    template_name = "torneo/arbitro/agregar.html"
    success_url = reverse_lazy('torneo_app:listar_arbitro')


#clase para ver los datos en detalle de un solo equipo
# utilizaremos un DetaiView que se encarga de recibir el id de equipo
class detalleArbitro(DetailView):
    # pasamos hatml donde se pintara el detalle del objeto
    template_name = 'torneo/arbitro/detalle.html'
    #pasamos el modelo o tabla del objeto
    model = Arbitro


class ModificarArbitro(UpdateView):
    #le especificamos la tabla de BD
    model = Arbitro
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'torneo/arbitro/modificar.html'
    success_url = reverse_lazy('torneo_app:listar_arbitro')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = ArbitroForm


class EliminarArbitro(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'torneo/arbitro/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = Arbitro
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('torneo_app:listar_arbitro')
