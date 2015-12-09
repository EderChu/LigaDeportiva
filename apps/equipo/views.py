# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy, reverse

from .forms import FacultadForm, EquipoForm
from apps.equipo.models import Facultad, Equipo

from django.http import HttpResponseRedirect
from django.utils import timezone


#manteimiento facultad
class ListFacultad(ListView):
    context_object_name = 'facultades'
    queryset = Facultad.objects.all()
    template_name = 'equipo/facultad/listar.html'


#clase para registrar un equipo utilizando createview
class RegistrarFacultad(CreateView):
    form_class = FacultadForm
    template_name = "equipo/facultad/agregar.html"
    success_url = reverse_lazy('equipo_app:listar-facultad')


class detalleFacultad(DetailView):
    # pasamos hatml donde se pintara el detalle del objeto
    template_name = 'equipo/facultad/detalle.html'
    #pasamos el modelo o tabla del objeto
    model = Facultad


class ModificarFacultad(UpdateView):
    #le especificamos la tabla de BD
    model = Facultad
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'equipo/facultad/modificar.html'
    success_url = reverse_lazy('equipo_app:listar-facultad')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = FacultadForm


class EliminarFacultad(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'equipo/facultad/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = Facultad
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('equipo_app:listar-facultad')


# modificar equipo
class ActualizarEquipo(FormView):
    template_name = 'equipo/equipo/modificar.html'
    form_class = EquipoForm
    success_url = '.'

    def get_initial(self):
        # recuperamos el objeto equipo
        initial = super(ActualizarEquipo, self).get_initial()
        usuario = self.request.user
        # recuperamos las observaciones
        equipo_query = Equipo.objects.filter(junta_directiva__presidente=usuario)
        if equipo_query.count() > 0:
            equipo = equipo_query[0]
            initial['nombre'] = equipo.nombre
            initial['color_camiseta'] = equipo.color_camiseta
            initial['junta_directiva'] = equipo.junta_directiva
            initial['comando_tecnico'] = equipo.comando_tecnico
            initial['facultad'] = equipo.facultad
            initial['logo'] = equipo.logo
        return initial

    def form_valid(self, form):
        usuario = self.request.user
        # recuperamos las observaciones
        equipo_query = Equipo.objects.filter(junta_directiva__presidente=usuario)
        if equipo_query.count() > 0:
            equipo = equipo_query[0]
            equipo.nombre = form.cleaned_data['nombre']
            equipo.color_camiseta = form.cleaned_data['color_camiseta']
            equipo.junta_directiva = form.cleaned_data['junta_directiva']
            equipo.comando_tecnico = form.cleaned_data['comando_tecnico']
            equipo.facultad = form.cleaned_data['facultad']
            equipo.logo = form.cleaned_data['logo']
            # guaranos el equipo con los nuevos datos
            equipo.save()
        return super(ActualizarEquipo, self).form_valid(form)