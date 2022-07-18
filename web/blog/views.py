from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q

from .models import cursos_dictados
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

def cv(request):
    #return HttpResponse('aca va mi CV')
    return render(request, "blog/cv.html", {})

def acerca(request):
    #return HttpResponse('aca va info acerca de mi')
    return render(request, "blog/acerca.html", {})

def post(request):

    return render(request, "blog/post.html", {})

