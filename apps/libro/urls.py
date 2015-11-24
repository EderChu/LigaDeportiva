# -*- encoding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^autor-add/$',
        views.AgregarAutor.as_view(),
        name='autor-add'
    ),
    url(
        r'^autor-list/$',
        views.ListAutorView.as_view(),
        name='listar-autor'
    ),
    url(
        r'^autor-update/(?P<pk>\d+)$',
        views.ModificarAutor.as_view(),
        name='update-autor'
    ),
    url(
        r'^autor-delete/(?P<pk>\d+)$',
        views.EliminarAutor.as_view(),
        name='delete-autor'
    ),
#urls para editorial
    url(
        r'^editorial-add/$',
        views.AgregarEditorial.as_view(),
        name='editorial-add'
    ),
    url(
        r'^editorial-list/$',
        views.ListEditorialView.as_view(),
        name='listar-editorial'
    ),
    url(
        r'^editorial-update/(?P<pk>\d+)$',
        views.ModificarEditorial.as_view(),
        name='update-editorial'
    ),
    url(
        r'^editorial-delete/(?P<pk>\d+)$',
        views.EliminarEditorial.as_view(),
        name='delete-editorial'
    ),
#urls para libro
    url(
        r'^libro-add/$',
        views.AgregarLibro.as_view(),
        name='libro-add'
    ),
    url(
        r'^libro-list/$',
        views.ListLibroView.as_view(),
        name='listar-libro'
    ),
    url(
        r'^libro-update/(?P<pk>\d+)$',
        views.ModificarLibro.as_view(),
        name='update-libro'
    ),
    url(
        r'^libro-delete/(?P<pk>\d+)$',
        views.EliminarLibro.as_view(),
        name='delete-libro'
    ),
]