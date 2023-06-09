from django import forms
from .models import Comunicado

class ComunicadoForm(forms.ModelForm):
    contenido = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Comunicado
        fields = ['titulo', 'contenido', 'categoria']
