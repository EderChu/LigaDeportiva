from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^equipo/$',
        views.RegistrarEquipo.as_view(),
        name='equipo'
    ),
    url(
        r'^jugador/$',
        views.RegisterJugador.as_view(),
        name='jugador'
    ),
    ]