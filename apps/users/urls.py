from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.InicioView.as_view(),
        name='inicio'
    ),
    ]