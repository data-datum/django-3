from django.db import models

# Create your models here.

class cursos_dictados(models.Model):
    curso = models.CharField("Nombre", max_length=200)
    horas = models.PositiveIntegerField("Horas")
    institucion = models.CharField("Institucion", max_length=200)
    anio = models.DateTimeField("Año", max_length=4)

class workshops(models.Model):
    workshop = models.CharField("Nombre", max_length=200)
    horas = models.PositiveIntegerField("Horas")
    congreso = models.CharField("Congreso", max_length=200)
    anio = models.DateTimeField("Año", max_length=4)

    