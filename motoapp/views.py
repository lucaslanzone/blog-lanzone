from dataclasses import fields
from unicodedata import name
from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from sqlite3 import Cursor
from motoapp.models import Pruebas, Lanzamientos, Mercado
from motoapp.forms import pruebasFormulario, UsuarioRegistroForm, UsuarioEditForm

#Vistas basadas en clases

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Para el Login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicio(request):
    dict_ctx = {"title": "Inicio", "message": "MOTOBLOG"}
    return render(request, "motoapp/index.html", dict_ctx)

@login_required()
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
           
@login_required
def Lanzamientos(request):
    
    dict_ctx = {"title": "Lanzamientos", "message": "Lanzamientos"}
    return render(request, "motoapp/lanzamientos.html", dict_ctx)

@login_required
def Mercado(request):
    
    dict_ctx = {"title": "Mercado", "message": "Mercado"}
    return render(request, "motoapp/mercado.html", dict_ctx)

@login_required
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
    

      
      
      
@login_required      
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


class PruebasLista(LoginRequiredMixin ,ListView):

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


def login_request(request):

    if request.method == "POST":
        formulario = AuthenticationForm(request, data= request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get('username')
            contrasenia = data.get('password')

            
            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)

                dict_ctx = {"title": "Inicio", "page": usuario }
                return render(request, "motoapp/index.html", dict_ctx)

            else:
                dict_ctx = {"title": "Inicio", "page": usuario, "errors": ["El usuario no existe"]}
                return render(request, 'motoapp/index.html', dict_ctx)
        else:
            dict_ctx = {"title": "Inicio", "page": "anonymous", "errors": ["Revise los datos cargados en el form"]}
            return render(request, 'motoapp/index.html', dict_ctx)

    
    else:
        form = AuthenticationForm()
        return render(request, "motoapp/login.html", {"form": form})



def register_request(request):

    if request.method == "POST":

      form = UsuarioRegistroForm(request.POST)

      if form.is_valid():
          usuario = form.cleaned_data.get("username")
          print(usuario)
          form.save()
          return redirect("Inicio")

    
      else:
           dict_ctx = {"title": "Inicio", "page": "anonymous", "errors": ["No paso las validaciones"]}
           return render(request, "motoapp/index.html", dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request, "motoapp/register.html", {"form": form})

@login_required
def actualizar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]

            usuario.save

            return redirect("Inicio")

        else:
            formulario = UsuarioEditForm(initial={"email": usuario.email})
            return render(request, "motoapp/editar_usuario.html", {"form": formulario, "errors": ["Datos incorrectos"]})

    else:
        formulario = UsuarioEditForm(initial={"email": usuario.email})
        return render(request, "motoapp/editar_usuario.html", {"form": formulario})