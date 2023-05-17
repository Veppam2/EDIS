from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mesa

class AgregarNombre(forms.Form):
    nombre = forms.CharField(label = 'ingresa tu nombre', max_length =10)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username', "first_name", "last_name","email", "password1", "password2"]

class MesaForm(forms.Form):
    class Meta:
        model= Mesa
        fields =['numero_mesa', "ubicacion"]


class MesaForm2(forms.Form):
    numero_mesa = forms.IntegerField(
        label = "Número de Mesa",
        required = True,
    )
    ubicacion = forms.CharField(
        label = "Ubicación",
        required = True,
        max_length = 100
    )
