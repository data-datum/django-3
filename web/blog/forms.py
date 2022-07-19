
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NuevoCurso(forms.Form):
    curso = forms.CharField(max_length=200, label="Nombre")
    horas = forms.IntegerField(min_value=0)
    institucion = forms.CharField(max_length=200, label="Institucion")
    anio = forms.IntegerField(min_value=0, label="Año")

class NuevoWorkshop(forms.Form):
    workshop = forms.CharField(max_length=200, label="Nombre")
    horas = forms.IntegerField(min_value=0)
    congreso = forms.CharField(max_length=200, label="Congreso")
    anio = forms.IntegerField(min_value=0, label="Año")

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) #la contraseña no se ve
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        #help_texts ={k: "" for k in fields}