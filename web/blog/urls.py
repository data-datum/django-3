from django.urls import path
from django.urls import path, include

from blog.views import * 

urlpatterns = [
    #URLs de la app
    path('cursos/', cursos),
    path('cv/', cv),
    path('acerca/', acerca),
]