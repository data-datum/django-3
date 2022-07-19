from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q

from .models import *
# Create your views here.


def index(request):
    
    return render(request, "blog/index.html", {})

def cursos(request):
    #return HttpResponse('aca van los cursos de posgrado que dicte')

    if request.method == "POST":

        search = request.POST["search"]

        if search !="":
            cursos = cursos_dictados.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search)).values()

            return render(request, "blog/cursos.html", {"cursos":cursos, "search":True, "busqueda":search})
  

    cursos = cursos_dictados.objects.all()
    ctx = {'cursos':cursos}

    return render(request, "blog/cursos.html", ctx)

def agregar_curso(request):

    if request.method == "POST":

        info_formulario = request.POST

        cursos = cursos_dictados(curso=str(info_formulario["curso"]), horas=int(info_formulario["horas"]), institucion=str(info_formulario["institucion"]), anio=int(info_formulario["anio"]))

        cursos.save()

        return render(request, "blog/agregar_curso.html", {})

    else:
        return render(request, "blog/agregar_curso.html", {})


def cv(request):
    #return HttpResponse('aca va mi CV')
    return render(request, "blog/cv.html", {})

def acerca(request):
    #return HttpResponse('aca va info acerca de mi')
    return render(request, "blog/acerca.html", {})

def post(request):

    return render(request, "blog/post.html", {})

