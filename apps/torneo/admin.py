from django.contrib import admin

from .models import Torneo, Arbitro, CampoDeportivo, Fixture, Persona, PrecioPago


# Register your models here.
admin.site.register(Torneo)
admin.site.register(Arbitro)
admin.site.register(CampoDeportivo)
admin.site.register(Fixture)
admin.site.register(Persona)
admin.site.register(PrecioPago)
