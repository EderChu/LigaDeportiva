# -*- encoding: utf-8 -*-
from django import forms
from apps.equipo.models import Facultad, Equipo, ComandoTecnico, JuntaDirectiva
from apps.torneo.forms import PersonaForm


class FacultadForm(forms.ModelForm):

    class Meta:
        model = Facultad
        fields = ("__all__")

    def clean_nombre(self):
        nom = self.cleaned_data['nombre']
        num_palabras = len(nom)
        if num_palabras < 5:
            raise forms.ValidationError("nombre muy corto")
        return nom

    def clean_prop(self):
        sig = self.cleaned_data['propietario']
        num_palabras = len(sig)
        if num_palabras > 2:
            raise forms.ValidationError("Sigla no valida")
        return prop


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ('__all__')

class ComandoTecnicoForm(forms.ModelForm):
    class Meta:
        model = ComandoTecnico
        fields = ('__all__')

class JuntaDirectivaForm(forms.ModelForm):
    class Meta:
        model = JuntaDirectiva
        fields = ('__all__')
