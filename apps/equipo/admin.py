from django.contrib import admin

# Register your models here.
from .models import ComandoTecnico, Equipo, Facultad, JuntaDirectiva, Pago

admin.site.register(ComandoTecnico)
admin.site.register(Equipo)
admin.site.register(Facultad)
admin.site.register(JuntaDirectiva)
admin.site.register(Pago)
