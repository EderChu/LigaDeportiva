from django.conf.urls import url
from . import views


urlpatterns = [
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
]
