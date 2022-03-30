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

            pruebas_nuevo = pruebas(data['marca'], data['modelo'], data['calificacion'])
            pruebas_nuevo.save()

        return render(request, 'motoapp/index.html')

    else: 
        pruebas_form = pruebasFormulario()

        return render(request, 'motoapp/pruebasFormulario.html', {"formulario": pruebas_form})

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


