from django import forms
from models import Equipo, Jugador, Medico, Especialidad

class EquipoForm(forms.ModelForm):
   class Meta:
        model = Equipo
        fields = (
            'nombre',
            'facultad',
            'delegado',
        )

   
   def clean_nombre(self):
       nom = self.cleaned_data['nombre']
       num_palabras = len(nom)
       if num_palabras<5:
             raise forms.ValidationError("nombre muy corto")
       return nom   
       
class JugadorForm(forms.Form):
    nombres = forms.CharField(max_length=50)
    apellidos = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField()
    equipo = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        super(JugadorForm, self).__init__(*args, **kwargs)
        #aqui es donde le digo que lene el combo box de la tabla
        self.fields['equipo'].queryset = Equipo.objects.all()

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ("__all__")

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ("__all__")
    
class BuscarForm(forms.Form):
       # TODO: Define form fields here
    clave = forms.CharField(label='Nombre',required=True)