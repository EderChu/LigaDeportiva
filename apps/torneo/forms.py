# -*- encoding: utf-8 -*-
from django import forms
from models import CampoDeportivo,Arbitro


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
class ArbitroForm(forms.ModelForm):

    class Meta:
        model = Arbitro
        fields = ("__all__")