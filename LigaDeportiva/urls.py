from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # urls para la aplicacion asistencia
    url(r'^', include('apps.users.urls', namespace="users_app")),
    # url(r'^', include('apps.prueba.urls', namespace="prueba_app")),
    # urls para la aplicacion users
    url(r'^', include('apps.torneo.urls', namespace="torneo_app")),
    url(r'^', include('apps.equipo.urls', namespace="equipo_app")),
    # url(r'^', include('apps.libro.urls', namespace="libro_app")),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    ]
