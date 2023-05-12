from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.contrib import messages

from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
def adminLogin(request):
    return redirect('/admin')

def index(request):
    return render(request, 'index.html')

@login_required
def paginaUno(request):
    return render(request, 'pagina1.html')


def registro(request):
    data = {'form': CustomUserCreationForm() }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid() :
            usuario = formulario.save()
            usuario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"],
            )
            login(request,user)
            messages.success(
                request,"Registro exitoso, inicia sesión"
            )
            return redirect(to="cincuentaAmigos:P1")
        data["form"]= formulario
    return render(request,'registration/registration.html', data)
