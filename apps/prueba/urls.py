from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^equipo/$',
        views.RegistrarEquipo.as_view(),
        name='registrar_equipo'
    ),
    url(
        r'^equipo/listar$',
        views.ListEquipo.as_view(),
        name='listar_equipo'
    ),
    url(
        r'^equipo/detalle/(?P<pk>\d+)$',
        views.DetalleEquipo.as_view(),
        name='detalle_equipo'
    ),
    url(
        r'^equipo/modificar/(?P<pk>\d+)$',
        views.ModificarEquipo.as_view(),
        name='modificar_equipo'
    ),
    url(
        r'^equipo/eliminar/(?P<pk>\d+)$',
        views.EliminarEquipo.as_view(),
        name='eliminar_equipo'
    ),

    ####### URL QUE LE CORRESPONDE A LA TABLA JUGADOR ################
    url(
        r'^jugador/$',
        views.RegisterJugador.as_view(),
        name='registrar_jugador'
    ),
    url(
        r'^jugador/listar$',
        views.ListJugador.as_view(),
        name='listar_jugador'
    ),
    ]