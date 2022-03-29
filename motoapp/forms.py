from django import forms

class lanzamientosFormulario(forms.Form):

    fecha = forms.DateField()
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)