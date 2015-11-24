# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy, reverse

from apps.torneo.forms import CampoDForm, CampoDeportivo, ArbitroForm, Arbitro


from django.http import HttpResponseRedirect
from django.utils import timezone


# Create your views here.
#Mantenimientos del campo deportivo
class ListarCampoD(ListView):
    context_object_name = 'campos'
    queryset = CampoDeportivo.objects.all()
    template_name = 'torneo/campodeportivo/listar.html'


#clase para registrar un equipo utilizando createview
class RegistrarCampoD(CreateView):
    form_class = CampoDForm
    template_name = "torneo/campodeportivo/agregar.html"
    success_url = reverse_lazy('torneo_app:listar_CampoD')


#clase para ver los datos en detalle de un solo equipo
# utilizaremos un DetaiView que se encarga de recibir el id de equipo
class detalleCampoD(DetailView):
    # pasamos hatml donde se pintara el detalle del objeto
    template_name = 'torneo/campodeportivo/detalle.html'
    #pasamos el modelo o tabla del objeto
    model = CampoDeportivo


#clase para modificar un registro de una tabla
#utilizamos UpdateView que se encarga de recuperar el objeto y actualizarlo
class ModificarCampoD(UpdateView):
    #le especificamos la tabla de BD
    model = CampoDeportivo
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'torneo/campodeportivo/modificar.html'
    success_url = reverse_lazy('torneo_app:listar_CampoD')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = CampoDForm


#clase para eliminar un registro de la BD
#utilizamos DeleteView que se encarga de recibir y elimnar los dato de la BD
class EliminarCampoD(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'torneo/campodeportivo/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = CampoDeportivo
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('torneo_app:listar_CampoD')

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


#clase para modificar un registro de una tabla
#utilizamos UpdateView que se encarga de recuperar el objeto y actualizarlo
class ModificarArbitro(UpdateView):
    #le especificamos la tabla de BD
    model = Arbitro
    # le pasamos el template donde se pintaran los datos recureados
    template_name = 'torneo/arbitro/modificar.html'
    success_url = reverse_lazy('torneo_app:listar_arbitro')
    #le pasamos el formulario en el que recibiremos los datos a modificar
    form_class = ArbitroForm


#clase para eliminar un registro de la BD
#utilizamos DeleteView que se encarga de recibir y elimnar los dato de la BD
class EliminarArbitro(DeleteView):
    #pasamos el template donde se mostraara los datos que vamos a eliminar
    template_name = 'torneo/arbitro/eliminar.html'
    #pasamos el modelo del cual se eliminara elregistro
    model = Arbitro
    #donde ira cuando se complete la accion
    success_url = reverse_lazy('torneo_app:listar_arbitro')
