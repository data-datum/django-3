from django.shortcuts import render
from django.http import HttpResponse

from .models import cursos_dictados
# Create your views here.


def index(request):
    
    return render(request, "blog/index.html", {})

def cursos(request):
    #return HttpResponse('aca van los cursos de posgrado que dicte')

    cursos = cursos_dictados.objects.all()
    ctx = {'cursos':cursos}

    return render(request, "blog/cursos.html", ctx)

def cv(request):
    #return HttpResponse('aca va mi CV')
    return render(request, "blog/cv.html", {})

def acerca(request):
    #return HttpResponse('aca va info acerca de mi')
    return render(request, "blog/acerca.html", {})

