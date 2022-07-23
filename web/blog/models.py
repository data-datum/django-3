from django.db import models
from django.contrib.auth.models import User


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


# modelo del avatar
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

    def __str__(self) -> str:
        return f"Usuario: {self.usuario}"

    class Meta:
        verbose_name_plural = "Avatar"