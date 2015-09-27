from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, ListView
from django.views.generic.edit import FormView, FormMixin
from django.core.urlresolvers import reverse_lazy

from django.utils import timezone

from .models import Equipo, Jugador

from .forms import *

# Create your views here.
class RegistrarEquipo(CreateView):
    form_class = EquipoForm
    template_name = "prueba/equipo.html"
    success_url = reverse_lazy('users_app:inicio')

class RegisterJugador(FormView):
    template_name = "prueba/jugador.html"
    form_class = JugadorForm
    success_url = reverse_lazy('prueba_app:jugador')

    def form_valid(self, form):
        nom = form.cleaned_data['nombres']
        apellido = form.cleaned_data['apellidos']
        nacimiento = form.cleaned_data['fecha_nacimiento']
        equipo = form.cleaned_data['equipo']

        jugador = Jugador(
                    nombres=nom,
                    apellidos=apellido,
                    fecha_nacimiento=nacimiento,
                    equipo=equipo        
                        )
        jugador.save()

        numero_jugadores = equipo.num_jugadores + 1
        equipo.save()

        return super(RegisterJugador,self).form_valid(form)
        
        