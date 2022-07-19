from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db.models import Q

from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm #formulario de autenticacion
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def index(request):

    return render(request, "blog/index.html")
    

def login_request(request):

    if request.method == "POST":

        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
    
    form = AuthenticationForm()


    return render (request, "blog/login.html",{"form":form})

def cursos(request):
    #return HttpResponse('aca van los cursos de posgrado que dicte')

    if request.method == "POST":

        search = request.POST["search"]

        if search !="":
            cursos = cursos_dictados.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search)).values()

            return render(request, "blog/cursos.html", {"cursos":cursos, "search":True, "busqueda":search})
  

    cursos = cursos_dictados.objects.all()
    #ctx = {'cursos':cursos}

    return render(request, "blog/cursos.html", {"cursos":cursos})

def agregar_curso(request):

    if request.method == "POST":

        info_formulario = request.POST

        cursos = cursos_dictados(curso=str(info_formulario["curso"]), horas=int(info_formulario["horas"]), institucion=str(info_formulario["institucion"]), anio=int(info_formulario["anio"]))

        cursos.save()

        return render(request, "blog/agregar_curso.html", {})

    else:
        return render(request, "blog/agregar_curso.html", {})

def eliminar_curso(request, curso_id):

    # post
    curso = curso.objects.get(id=curso_id)
    curso.delete()

    return redirect("cursos")

def editar_curso(request, curso_id):

    # post
    
    curso = curso.objects.get(id=curso_id)

    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
        
            curso.curso = info_curso["curso"]
            curso.anio = info_curso["anio"]
            curso.save() # guardamos en la bd
            
            return redirect("cursos")

            
    formulario = NuevoCurso(initial={"nombre":curso.curso,"comision":curso.anio})

    return render(request,"blog/agregar_curso.html",{"form":formulario,"accion":"Editar Curso"})

def cv(request):
    #return HttpResponse('aca va mi CV')
    return render(request, "blog/cv.html", {})

def acerca(request):
    #return HttpResponse('aca va info acerca de mi')
    return render(request, "blog/acerca.html", {})

def post(request):

    return render(request, "blog/post.html", {})

