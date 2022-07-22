from django.urls import path
from django.urls import path, include

from .views import * 

urlpatterns = [
    #URLs de la app
    #path('', inicio),
    path('', index, name="index"),
    path('login/', login_request, name="login"),
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"), 
    path('cursos/', cursos, name="cursos"),
    path('agregar_curso/', agregar_curso, name="agregar_curso"),
    path('eliminar_curso/<curso_id>/', eliminar_curso, name="eliminar_curso"),
    path('editar_curso/<curso_id>/', editar_curso, name="editar_curso"),
    path('cv/', cv, name="cv"),
    path('acerca/', acerca, name="acerca"),
    path('posts/', posts, name="posts"),
    path('post', post, name="post"),
    path('post2', post2, name="post2"),
    path('post3', post3, name="post3"),
    path('post4', post4, name="post4"),
]