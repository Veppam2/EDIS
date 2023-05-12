from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AgregarNombre(forms.Form):
    nombre = forms.CharField(label = 'ingresa tu nombre', max_length =10)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields =['username', "first_name", "last_name","email", "password1", "password2"]
