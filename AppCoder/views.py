from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

from AppCoder.forms import CursoForm

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

"""def cursoFormulario(request):
    if request.method== "POST":
        nombre= request.POST["nombre"]
        comision= request.POST["comision"]
        print(nombre, comision)
        curso= Curso (nombre= nombre, comision= comision)
        curso.save
        return render (request, "AppCoder/inicio.html", {"mensaje": "Curso guardado correctamente"})
    else:
        return render (request, "AppCoder/cursoFormulario.html")"""

def cursoFormulario(request):
    if request.method== "POST":
        form= CursoForm(request.POST)
        if form.is_valid():
            informacion= form.cleaned_data
            print(informacion)
            nombre= informacion["nombre"]
            comision= informacion["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save
            return render (request, "AppCoder/inicio.html", {"mensaje": "Curso guardado correctamente"})
        else:
            return render (request, "AppCoder/cursoFormulario.html", {"form": formulario})
    else:
        formulario= CursoForm()
        return render (request, "AppCoder/cursoFormulario.html", {"form": form, "mensaje": "Informacion no valida"})


def busquedaComision(request):
    return render (request, "AppCoder/busquedaComision.html")


def buscar(request):
    comision= request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__icontains=comision)
        return render (request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    
    else:
        return render (request, "AppCoder/busquedaComision.html", {"mensaje": "Che ingresa una comision para buscar!"})