from django.shortcuts import render
from django.http import HttpResponse
from sqlite3 import Cursor
from motoapp.models import pruebas, lanzamientos, mercado
from motoapp.forms import pruebasFormulario

# Create your views here.
def inicio(request):
    dict_ctx = {"title": "Inicio", "message": "MOTOBLOG"}
    return render(request, "motoapp/index.html", dict_ctx)

def pruebas(request):
    
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
           

def lanzamientos(request):
    
    dict_ctx = {"title": "Lanzamientos", "message": "Lanzamientos"}
    return render(request, "motoapp/lanzamientos.html", dict_ctx)

def mercado(request):
    
    dict_ctx = {"title": "Mercado", "message": "Mercado"}
    return render(request, "motoapp/mercado.html", dict_ctx)

def formulario_pruebas(request):

    if request.method == "POST":
        pruebas = pruebasFormulario(request.POST)
        print(pruebas)

        if pruebas.is_valid:
            data = pruebas.cleaned_data

            prueba_nueva = prueba_nueva(data['marca'], data['modelo'], data['calificacion'])
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


