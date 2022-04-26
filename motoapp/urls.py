from operator import index
from django.urls import path
from unicodedata import name
from motoapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="motoapp/logout.html"), name="logout"),
    path('register/', register_request, name="register"),
    path('pruebas/', Pruebas, name="Pruebas"),
    path('lanzamientos/', Lanzamientos, name="Lanzamientos"),
    path('mercado/', Mercado, name="Mercado"),
    path('pruebasFormulario/', formulario_pruebas, name='Formulario'),
    path('buscarpruebas/', buscarpruebas, name='buscarpruebas'),
    path('borrarpruebas/<marca_id>/', borrar_pruebas, name="eliminarPrueba" ),
    path('update_prueba/<marca_id>/', actualizar_pruebas),


    path("pruebas/list", PruebasLista.as_view(), name="pruebas_list"),
    path("pruebas/nuevo/", PruebasCrear.as_view(), name="pruebas_create"),
    path("pruebas/detalle/<pk>/", PruebasDetalle.as_view(), name="pruebas_detail"),
    path("pruebas/editar/<pk>/", PruebasActualizar.as_view(), name="pruebas_update"),
    path("pruebas/borrar/<pk>/", PruebasBorrar.as_view(), name="pruebas_delete"),
]
