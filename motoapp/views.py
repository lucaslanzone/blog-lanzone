from dataclasses import fields
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from sqlite3 import Cursor
from motoapp.models import Pruebas, Lanzamientos, Mercado
from motoapp.forms import pruebasFormulario

#Vistas basadas en clases

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
def inicio(request):
    dict_ctx = {"title": "Inicio", "message": "MOTOBLOG"}
    return render(request, "motoapp/index.html", dict_ctx)

def Pruebas(request):

    dict_ctx = {"title": "Pruebas", "message": "Pruebas"}
    return render(request, "motoapp/pruebas.html", dict_ctx)

    pruebas = pruebas.objects.all()

    if request.method == "POST":
        pruebas = pruebasFormulario(request.POST)

        if pruebas.is_valid():
            data = pruebas.cleaned_data

            pruebas = pruebas(data['marca'], data['modelo'], data['calificacion'])
            pruebas.save()

            pruebas = pruebasFormulario()
            return render(request, "motoapp/pruebas.html", {"pruebas": pruebas, "title": "Pruebas", "page": "pruebas", "formulario": formulario})

        else:

            pruebas = pruebasFormulario()
            return render(request, "motoapp/pruebas.html", {"pruebas": pruebas, "title": "Pruebas", "page": "pruebas", "formulario": formulario})
           

def Lanzamientos(request):
    
    dict_ctx = {"title": "Lanzamientos", "message": "Lanzamientos"}
    return render(request, "motoapp/lanzamientos.html", dict_ctx)

def Mercado(request):
    
    dict_ctx = {"title": "Mercado", "message": "Mercado"}
    return render(request, "motoapp/mercado.html", dict_ctx)

def formulario_pruebas(request):

    if request.method == "POST":
        pruebas = pruebasFormulario(request.POST)
        print(pruebas)

        if pruebas.is_valid():
            data = pruebas.cleaned_data

            prueba_nueva = Pruebas(marca=data['marca'], modelo=data['modelo'], calificacion=data['calificacion'])
            prueba_nueva.save()

            return render(request, 'motoapp/index.html') 
            
            
    else:   
             formulario = pruebasFormulario()
             
    return render(request, 'motoapp/pruebasFormulario.html', {"formulario": pruebasFormulario}) 
    

      
      
      
      
def buscarpruebas(request):

    data = request.GET.get('marca', "")
    error = ""
    

    if data:
        try:
        
            pruebas = pruebasFormulario.objects.get(marca = data)
        
            return render(request, 'motoapp/buscarpruebas.html', {"pruebas": pruebas, "id": data})

        except Exception as exc:
            print(exc)
            error = "Prueba no encontrada"

    return render(request, 'motoapp/buscarpruebas.html', {"error": error})


def borrar_pruebas(request, marca_id):
    try:
       pruebas = Pruebas.object.get(marca=marca_id)
       pruebas.delete()
       return render(request, "motoapp/index.html")
    except Exception as exc:
        return render(request, "motoapp/index.html")


def actualizar_pruebas(request, marca_id):

    pruebas = Pruebas.objects.get(marca=marca_id)

    if request.method == "POST":
        formulario = pruebasFormulario(request.POST)

        if formulario.is_valid():

            informacion = formulario.cleaned_data

            pruebas.marca = informacion["marca"]

            pruebas.save()

            return render(request, "motoapp/index.html")
            

    else:

        formulario = pruebasFormulario(initial={"marca": pruebas.marca, "modelo": pruebas.modelo, "calificacion": pruebas.calificacion})

        return render(request, "motoapp/update_prueba.html", {"formulario": formulario, "marca_id":marca_id})


class PruebasLista(ListView):

    model = Pruebas
    template_name = "/motoapp/pruebas_list.html"

class PruebasDetalle(DetailView):

    model = Pruebas
    template_name = "/motoapp/pruebas_detalle.html"

class PruebasCrear(CreateView):

    model = Pruebas
    success_url = "/motoapp/pruebas/list"
    fields = ['marca', 'modelo', 'calificacion'] 
    
class PruebasActualizar(UpdateView):

    model = Pruebas
    success_url = "/motoapp/pruebas/list"
    fields = ['calificacion']

class PruebasBorrar(DeleteView):
    model = Pruebas
    success_url = "/motoapp/pruebas/list"