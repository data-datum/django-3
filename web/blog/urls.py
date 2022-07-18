from django.urls import path
from django.urls import path, include

from .views import * 

urlpatterns = [
    #URLs de la app
    #path('', inicio),
    path('', index, name="index"),
    path('cursos/', cursos, name="cursos"),
    path('agregar_curso', agregar_curso, name="agregar_curso"),
    path('cv/', cv, name="cv"),
    path('acerca/', acerca, name="acerca"),
    path('post/', post, name="post"),
]