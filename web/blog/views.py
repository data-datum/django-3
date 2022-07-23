from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db.models import Q

from .models import *
from .forms import *

from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def index(request):

    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(usuario=request.user)
            url = avatar.image.url
        except:
            url = "/media/avatar/generica.jpg"
        return render(request, "blog/index.html", {"url":url})
    
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
                return redirect("index")
            else:
                return redirect("login")
    
    form = AuthenticationForm()


    return render (request, "blog/login.html",{"form":form})


def register_request(request):

    if request.method == "POST":

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') #1er contraseña

            form.save() #registramos el usuario 
            #iniciamos la sesion
            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return redirect("login")

        return render(request, "blog/register.html", {"form":form})

    #form = UserCreationForm()
    form = UserRegisterForm(request.POST)

    return render(request, "blog/register.html", {"form":form})


def logout_request(request):
    logout(request)
    return redirect("index")


@login_required
def editar_perfil(request):

    user = request.user # usuario con el que estamos loggueados
    try:
        avatar = Avatar.objects.get(usuario=user)
    except:
        avatar = Avatar(usuario=user)
        avatar.save()

    if request.method == "POST":
        
        form = UserEditForm2(request.POST, request.FILES) # cargamos datos llenados

        if form.is_valid():

            info = form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]

            user.save()

            if info['imagen'] != None:
                avatar.imagen = info['imagen']
                avatar.save()

            return redirect("index")

        else:
            print(form.errors)
            return render(request, "blog/editar_perfil.html", {"form":form})

    else:
        form = UserEditForm2(initial={"email":user.email, "first_name":user.first_name, "last_name":user.last_name, "imagen":avatar.imagen})

    return render(request,"blog/editar_perfil.html",{"form":form})


def cursos(request):
    #return HttpResponse('aca van los cursos de posgrado que dicte')

    if request.method == "POST":

        search = request.POST["search"]

        if search !="":
            cursos = cursos_dictados.objects.filter( Q(curso__icontains=search) | Q(horas__icontains=search)).values()

            return render(request, "blog/cursos.html", {"cursos":cursos, "search":True, "busqueda":search})
  

    cursos = cursos_dictados.objects.all()
    #ctx = {'cursos':cursos}
    

    return render(request, "blog/cursos.html", {"cursos":cursos})

@staff_member_required
def agregar_curso(request):

    if request.method == "POST":
        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_formulario=formulario.cleaned_data

            cursos = cursos_dictados(curso=info_formulario["curso"],horas=info_formulario["horas"], institucion=info_formulario["institucion"], anio=info_formulario["anio"])
            cursos.save()
            return redirect("cursos")

        else: #get
        
            return render(request, "blog/agregar_curso.html", {"form":formulario,"accion":"Crear Curso"})
    else:

        formularioVacio=NuevoCurso()

        return render(request, "blog/agregar_curso.html", {"form":formularioVacio,"accion":"Crear Curso"})


@staff_member_required
def eliminar_curso(request, curso_id):

    # post
    curso = cursos_dictados.objects.get(id=curso_id)
    curso.delete()

    return redirect("cursos")


@staff_member_required
def editar_curso(request,curso_id):

    curso = cursos_dictados.objects.get(id=curso_id)

    if request.method == "POST":
        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data

            curso.curso = info_curso["curso"]
            curso.horas=info_curso["horas"]
            curso.institucion=info_curso["institucion"]
            curso.anio = info_curso["anio"]
            curso.save() # guardamos en la bd

            return redirect("cursos")


    #get
    formulario_vacio=NuevoCurso(initial={"nombre":curso.curso, 
                                    "horas": curso.horas, 
                                    "institucion":curso.institucion, 
                                    "anio":curso.anio})
    return render(request, "blog/agregar_curso.html", {"form": formulario_vacio})



@staff_member_required
def agregar_workshop(request):

    if request.method == "POST":

        info_formulario = request.POST

        workshops = workshops(curso=info_formulario["curso"],
                                 horas=info_formulario["horas"], 
                                 congreso=info_formulario["congreso"], 
                                 anio=info_formulario["anio"])

        workshops.save()

        return render(request, "blog/agregar_curso.html", {})

    else:
        return render(request, "blog/agregar_curso.html", {})



def cv(request):
    #return HttpResponse('aca va mi CV')
    return render(request, "blog/cv.html", {})

def acerca(request):
    #return HttpResponse('aca va info acerca de mi')
    return render(request, "blog/acerca.html", {})

def base(request):
    
    return render(request, "blog/base.html", {})

def base2(request):
    
    return render(request, "blog/base2.html", {})

def base4(request):
    
    return render(request, "blog/base4.html", {})
  

def posts(request):

    return render(request, "blog/posts.html", {})

def post(request):

    return render(request, "blog/post.html", {})

def post2(request):

    return render(request, "blog/post2.html", {})

def post3(request):

    return render(request, "blog/post3.html", {})

def post4(request):

    return render(request, "blog/post4.html", {})
