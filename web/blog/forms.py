from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class NuevoCurso(forms.Form):
    curso = forms.CharField(max_length=200, label="Nombre")
    horas = forms.IntegerField(min_value=0)
    institucion = forms.CharField(max_length=200, label="Institucion")
    anio = forms.DateField(label="Año")

class NuevoWorkshop(forms.Form):
    workshop = forms.CharField(max_length=200, label="Nombre")
    horas = forms.IntegerField(min_value=0)
    congreso = forms.CharField(max_length=200, label="Congreso")
    anio = forms.DateField(label="Año")

#formulario de registro
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput) #la contraseña no se ve
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        #help_texts ={k: "" for k in fields}


#formulario de edicion de registro
class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

        help_texts = {k:"" for k in fields}

class UserEditForm2(forms.Form):

    email = forms.EmailField(label="Email")
    imagen = forms.ImageField(label="Imagen", required=False)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

