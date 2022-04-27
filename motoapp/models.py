from email.headerregistry import UnstructuredHeader
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User

# Create your models here.
class Pruebas(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    calificacion = models.IntegerField()

class Lanzamientos(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    fecha = models.DateField()

class Mercado(models.Model):
    fecha = models.DateField
    noticia = models.TextField()
    
class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
