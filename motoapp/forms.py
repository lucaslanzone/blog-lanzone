from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class pruebasFormulario(forms.Form):

    
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=40)
    calificacion = forms.IntegerField()


class UsuarioRegistroForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contraseña 2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        