from django import forms

class pruebasFormulario(forms.Form):

    
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    calificacion = forms.IntegerField()