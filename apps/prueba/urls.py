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

##### urls de examen
    url(
        r'^especialidad/$',
        views.RegistrarEpecialidad.as_view(),
        name='registrar_especialidad'
    ),
    url(
        r'^especialidad/listar$',
        views.ListarEspecialidad.as_view(),
        name='listar_especialidad'
    ),
    # url(
    #     r'^especialidad/detalle/(?P<pk>\d+)$',
    #     views.DetalleEspecialidad.as_view(),
    #     name='detalle_especialidad'
    # ),
    # url(
    #     r'^especialidad/modificar/(?P<pk>\d+)$',
    #     views.ModificarEspecialidad.as_view(),
    #     name='modificar_equipo'
    # ),
    # url(
    #     r'^especialidad/eliminar/(?P<pk>\d+)$',
    #     views.EliminarEspecialidad.as_view(),
    #     name='eliminar_equipo'
    # ),

    url(
        r'^medico/$',
        views.RegistrarMedico.as_view(),
        name='registrar_medico'
    ),
    url(
        r'^medico/listar$',
        views.ListarMedico.as_view(),
        name='listar_medico'
    ),
    url(
        r'^medico/modificar/(?P<pk>\d+)$',
        views.ModificarMedico.as_view(),
        name='modificar_medico'
    ),
    url(
        r'^medico/eliminar/(?P<pk>\d+)$',
        views.EliminarMedico.as_view(),
        name='eliminar_medico',
     ),
    ]