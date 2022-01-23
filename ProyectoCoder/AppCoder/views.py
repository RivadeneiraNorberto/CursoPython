from django.http import HttpResponse, request
from django.shortcuts import render, redirect


from AppCoder.forms import CursoFormulario
from .models import Curso


# Create your views here.
# def curso(request):
#     curso = Curso(nombre="SQL Basico", camada=335984)
#     curso.save()
#     documentoTexto = f'Se guardó el Curso: {curso.nombre}  correspondiente a la Camada: {curso.camada}.'
    
#     return HttpResponse(documentoTexto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html', {'cursos' : Curso.objects.all()})

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def cursoFormulario(request):
    if request.method == 'POST':
        formulario =  CursoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Curso.objects.create(nombre=data['curso'], camada=data['camada'])
            return redirect('Cursos')
    else:
        formulario=CursoFormulario()

    return render(request, 'AppCoder/cursoFormulario.html', {'formulario':formulario}) 

def busquedaCamada(request):
    return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada=camada)
        
        return render(request, 'AppCoder/buscar.html', {'cursos':cursos, 'camada':camada})
    else:
        return HttpResponse(f'No enviaste un nro de camada para buscar.')