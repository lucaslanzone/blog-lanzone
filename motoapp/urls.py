from operator import index
from django.urls import path
from motoapp.views import *


urlpatterns = [
    path('', index, name="Index"),
    path('pruebas/', pruebas, name="Pruebas"),
    path('lanzamientos/', lanzamientos, name="Lanzamientos"),
    path('mercado/', mercado, name="Mercado"),
    path('lanzamientosFormulario/', formulario_lanzamiento, name='Formulario'),
    path('buscarlanzamiento/', buscarLanzamiento, name='BusquedaLanzamiento'),
]
