from django.http import HttpResponse
from django.template import loader


def inicio(request):
    return HttpResponse("Bienvenidos")