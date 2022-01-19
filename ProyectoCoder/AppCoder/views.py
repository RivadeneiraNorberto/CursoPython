from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(request):
    curso = Curso(nombre="SQL Basico", camada=335984)
    curso.save()
    documentoTexto = f'Se guardó el Curso: {curso.nombre}  correspondiente a la Camada: {curso.camada}.'
    
    return HttpResponse(documentoTexto)