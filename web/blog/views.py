from django.shortcuts import render
from django.http import HttpResponse

from .models import cursos_dictados
# Create your views here.


def index(request):
    cursos = cursos_dictados.objects.all()
    ctx = {'cursos':cursos}
    return render(request, "blog/index.html", ctx)

def cursos(request):
    return HttpResponse('aca van los cursos de posgrado que dicte')

def cv(request):
    return HttpResponse('aca va mi CV')

def acerca(request):
    return HttpResponse('aca va info acerca de mi')

