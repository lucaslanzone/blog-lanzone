from operator import index
from django.urls import path
from unicodedata import name
from motoapp.views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('pruebas/', pruebas, name="Pruebas"),
    path('lanzamientos/', lanzamientos, name="Lanzamientos"),
    path('mercado/', mercado, name="Mercado"),
    path('pruebasFormulario/', formulario_pruebas, name='Formulario'),
    path('buscarpruebas/', buscarpruebas, name='buscarpruebas'),
]
