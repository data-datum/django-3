from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.

class cursos_dictados(models.Model):
    curso = models.CharField("Nombre", max_length=200)
    horas = models.PositiveIntegerField("Horas")
    institucion = models.CharField("Institucion", max_length=200)
    anio = models.DateTimeField("Año", max_length=4)

    def __str__(self) -> str:
        return f"Curso: {self.nombre} en {self.anio}"

    class Meta:
        verbose_name_plural = "Cursos Dictados"

class workshops(models.Model):
    workshop = models.CharField("Nombre", max_length=200)
    horas = models.PositiveIntegerField("Horas")
    congreso = models.CharField("Congreso", max_length=200)
    anio = models.DateTimeField("Año", max_length=4)

    def __str__(self) -> str:
        return f"Workshop: {self.nombre} en {self.anio}"

    class Meta:
        verbose_name_plural = "Workshops"

class Posteo(models.Model):
    titulo = models.CharField("Título", max_length=200, blank=True, null=True)
    contenido = models.TextField("Contenido", blank=True, null=True)
    imagen = models.ImageField("Imagen", upload_to="blog_img/", blank=True, null=True)
    #fecha = models.DateTimeField(default=timezone.now)
    autor = models.CharField(max_length=50, blank=True, null=True)
   
    def __str__(self):
        return f"Título: {self.titulo}"

# modelo del avatar
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}"

    class Meta:
        verbose_name_plural = "Avatar"