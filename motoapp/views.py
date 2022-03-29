from django.shortcuts import render
from django.http import HttpResponse
from sqlite3 import Cursor
from motoapp.models import pruebas, lanzamientos, mercado
from motoapp.forms import lanzamientosFormulario

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

def formulario_lanzamiento(request):

    if request.method == "POST":
        lanzamientos = lanzamientosFormulario(request.POST)
        print(lanzamientos)

        if lanzamientos.is_valid:
            data = lanzamientos.cleaned_data

            lanzamientos_nuevo = lanzamientos(data['fecha'], data['marca'])
            lanzamientos_nuevo.save()

        return render(request, 'motoapp/index.html')

    else: 
        lanzamientos_form = lanzamientosFormulario()

        return render(request, 'motoapp/lanzamientosFormulario.html', {"formulario": lanzamientos_form})

def buscarlanzamiento(request):

    data = request.GET.get['fecha']
    error = ""
    print(data)

    if data:
        try:
        
            lanzamientos = lanzamientos.objects.get(fecha= data)
        
            return render(request, 'motoapp/busquedaLanzamientos.html', {"lanzamientos": lanzamientos, "id": data})

        except Exception as exc:
            print(exc)
            error = "Lanzamiento no encontrado"


    return render(request, 'motoapp/busquedaLanzamientos.html', {"error": error})


