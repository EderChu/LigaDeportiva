from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^facultad/$',
        views.RegistrarFacultad.as_view(),
        name='registrar-facultad'
    ),
    url(
        r'^facultad/listar/$',
        views.ListFacultad.as_view(),
        name='listar-facultad'
    ),
    url(
        r'^facultad/detalle/(?P<pk>\d+)$',
        views.detalleFacultad.as_view(),
        name='detalle-facultad'
    ),
    url(
        r'^facultad/modificar/(?P<pk>\d+)$',
        views.ModificarFacultad.as_view(),
        name='modificar-facultad'
    ),
    url(
        r'^facultad/eliminar/(?P<pk>\d+)$',
        views.EliminarFacultad.as_view(),
        name='eliminar-facultad',
    ),
] 