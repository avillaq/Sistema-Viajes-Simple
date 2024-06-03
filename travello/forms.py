from django import forms
from .models import DestinosTuristicos

class DestinosTuristicosForm(forms.ModelForm):
    class Meta:
        model = DestinosTuristicos
        fields = ['nombreCiudad', 'imagenCiudad', 'descripcionCiudad', 'precioTour', 'fechaTour', 'ofertaTour']
        widgets = {
            'fechaTour': forms.DateInput(attrs={'type': 'date'}),
        }