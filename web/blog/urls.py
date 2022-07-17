from django.urls import path
from django.urls import path, include

from .views import * 

urlpatterns = [
    #URLs de la app
    #path('', inicio),
    path('index/', index),
    path('cursos/', cursos),
    path('cv/', cv),
    path('acerca/', acerca),
]