from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(request):

    cursito= Curso(nombre="Python", comision=34645)
    cursito.save()
    cadena_texto=f"Curso guardardo: Nombre: {cursito.nombre}, Comision: {cursito.comision}"
    
    return HttpResponse (cadena_texto)

def cursos(request):
    return render (request, "AppCoder/cursos.html")

def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")

def inicio(request):
    return render (request, "AppCoder/inicio.html")