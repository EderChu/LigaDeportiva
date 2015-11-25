# -*- encoding: utf-8 -*-
from django import forms
from models import CampoDeportivo, Persona, Arbitro, Fixture, PrecioPago, Torneo


class CampoDForm(forms.ModelForm):

    class Meta:
        model = CampoDeportivo
        fields = ("__all__")

    def clean_nombre(self):
        nom = self.cleaned_data['nombre']
        num_palabras = len(nom)
        if num_palabras < 5:
            raise forms.ValidationError("nombre muy corto")
        return nom

    def clean_prop(self):
        prop = self.cleaned_data['propietario']
        num_palabras = len(prop)
        if num_palabras < 5:
            raise forms.ValidationError("Nombre de Propietario muy corto")
        return prop


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ("__all__")


class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = ("__all__")
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'datepicker'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'datepicker'}),
        }
