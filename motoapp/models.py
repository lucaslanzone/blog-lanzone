from django.db import models
from django.forms import CharField

# Create your models here.
class pruebas(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    calificacion = models.IntegerField()

class lanzamientos(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    fecha = models.DateField()

class mercado(models.Model):
    fecha = models.DateField
    noticia = models.CharField(max_length=120)
    