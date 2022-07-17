from django.urls import path
from django.urls import path, include

from .views import * 

urlpatterns = [
    #URLs de la app
    #path('', inicio),
    path('index/', index, name="index"),
    path('cursos/', cursos, name="cursos"),
    path('cv/', cv, name="cursos"),
    path('acerca/', acerca, name="acerca"),
]