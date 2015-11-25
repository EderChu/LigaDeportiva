# -*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    ####### URL QUE LE CORRESPONDE A LA TABLA CAMPO DEPORTIVO ################
    url(
        r'^torneo/registrar-campo-deportivo/$',
        views.RegistrarCampoD.as_view(),
        name='registrar_CampoD'
    ),
    url(
        r'^torneo/listar-campo-deportivo/$',
        views.ListarCampoD.as_view(),
        name='listar_CampoD'
    ),
    url(
        r'^campoD/detalle/(?P<pk>\d+)$',
        views.detalleCampoD.as_view(),
        name='detalle_CampoD'
    ),
    url(
        r'^campoD/modificar/(?P<pk>\d+)$',
        views.ModificarCampoD.as_view(),
        name='modificar_CampoD'
    ),
    url(
        r'^campoD/eliminar/(?P<pk>\d+)$',
        views.EliminarCampoD.as_view(),
        name='eliminar_CampoD',
    ),
    ####### URL QUE LE CORRESPONDE A LA TABLA PERSONA ################
    url(
        r'^persona/registrar$',
        views.RegistrarPersona.as_view(),
        name='registrar_persona'
    ),
    url(
        r'^persona/listar$',
        views.ListPersona.as_view(),
        name='listar-persona'
    ),
    url(
        r'^persona/detalle/(?P<pk>\d+)$',
        views.DetallePersona.as_view(),
        name='detalle_persona'
    ),
    url(
        r'^persona/modificar/(?P<pk>\d+)$',
        views.ModificarPersona.as_view(),
        name='modificar_persona'
    ),
    url(
        r'^persona/eliminar/(?P<pk>\d+)$',
        views.EliminarPersona.as_view(),
        name='eliminar_persona'
    ),
    ####### URL QUE LE CORRESPONDE A LA TABLA TORNEO ################
    url(
        r'^torneo/registrar$',
        views.RegistrarTorneo.as_view(),
        name='registrar_torneo'
    ),
    url(
        r'^torneo/listar$',
        views.ListTorneo.as_view(),
        name='listar_torneo'
    ),
    url(
        r'^torneo/detalle/(?P<pk>\d+)$',
        views.DetalleTorneo.as_view(),
        name='detalle_torneo'
    ),
    url(
        r'^torneo/modificar/(?P<pk>\d+)$',
        views.ModificarTorneo.as_view(),
        name='modificar_torneo'
    ),
    url(
        r'^torneo/eliminar/(?P<pk>\d+)$',
        views.EliminarTorneo.as_view(),
        name='eliminar_torneo'
    ),
]
