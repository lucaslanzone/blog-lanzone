from operator import index
from django.urls import path
from unicodedata import name
from motoapp.views import *


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('pruebas/', pruebas, name="Pruebas"),
    path('lanzamientos/', lanzamientos, name="Lanzamientos"),
    path('mercado/', mercado, name="Mercado"),
    path('lanzamientosFormulario/', formulario_lanzamiento, name='Formulario'),
    path('buscarlanzamiento/', buscarlanzamiento, name='BusquedaLanzamiento'),
]
