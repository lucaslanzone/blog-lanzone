from django.db import models
from django.forms import CharField

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
    