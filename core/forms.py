from django import forms

from .models import Clinica
 
class ClinicaForm(forms.ModelForm):

    class Meta:

        model = Clinica

        fields = ['nome', 'cnpj', 'endereco', 'telefone']
 