from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^panel/$',
        views.InicioView.as_view(),
        name='inicio'
    ),
    url(
        r'^$',
        views.LogIn.as_view(),
        name='login'
    ),
    url(
        r'^usuario/salir/$',
        'apps.users.views.LogOut',
        name='logout'
    ),
    url(
        r'^add-admin/$',
        views.AgregarAdministrador.as_view(),
        name='agregar-administrador'
    ),
]
