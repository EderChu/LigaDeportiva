# -*- encoding: utf-8 -*
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout

from django.core.urlresolvers import reverse_lazy

from apps.equipo.models import ComandoTecnico, JuntaDirectiva, Equipo

from .models import User
from .forms import LoginForm, RegistroUserForm, AdminEquipoForm
# Create your views here.


class InicioView(TemplateView):
    template_name = 'panel/panel.html'


class LogIn(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('users_app:inicio')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(LogIn, self).form_valid(form)


def LogOut(request):
    logout(request)
    return redirect('/')


class AgregarAdministrador(FormView):
    template_name = 'users/add-admin.html'
    form_class = RegistroUserForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        user.type_user = '1'
        user.set_password(form.cleaned_data['password1'])
        user.save()
        return super(AgregarAdministrador, self).form_valid(form)

    def form_invalid(self, form):
        print 'form eroors'
        return super(AgregarAdministrador, self).form_invalid(form)


class AgregarAdmiEquipo(FormView):
    template_name = 'users/admin_equipo.html'
    form_class = AdminEquipoForm
    success_url = '/'

    def form_valid(self, form):
        #guardamos el usuario
        user = form.save()
        user.type_user = '2'
        user.set_password(form.cleaned_data['password1'])
        user.save()
        team = form.cleaned_data['equipo']
        facultad = form.cleaned_data['facultad']
        if not team:
            #creamos junta directiva
            junta = JuntaDirectiva(
                presidente=user,
            )
            junta.save()
            print '==========junta guardada'
            #creamos comando tecnico
            comando = ComandoTecnico(
                junta_directiva=junta,
            )
            comando.save()
            print '==========comando guardado'
            #creamos equipo
            equipo = Equipo(
                junta_directiva=junta,
                comando_tecnico=comando,
                facultad=facultad,
            )
            equipo.save()
            print '==========equipo guardada'
            print 'Proceso Terminado'
        else:
            #recuperamos la junta del equipo
            junta = team.junta_directiva
            #actualizamos presidente de la junta
            junta.presidente = user
            junta.save()
            print '#######Proceso Terminado######'

        return super(AgregarAdmiEquipo, self).form_invalid(form)
