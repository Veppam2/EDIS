from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.contrib import messages

from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

from django.contrib.sessions.backends.db import SessionStore

s = SessionStore()

# Create your views here.
def adminLogin(request):
    return redirect('/admin')

def index(request):
    return render(request, 'index.html')

@login_required
def paginaUno(request):
    return render(request, 'pagina1.html')

def menuPrincipal(request):
    listaCategorias = Categoria.objects.all()
    print("menuprincipal")
    return render(request,
        'menu/menuPrincipal.html',
        {'listaCategorias': listaCategorias}
    )

def entradas(request):
    return render(request, 'menu/submenu.html')

def platillos(request):
    return render(request, 'menu/submenu.html')

def bebidas(request):
    return render(request, 'menu/submenu.html')

def postres(request):
    id_categoria = Categoria.objects.get(nombre = "Postres")
    lista_postres= Alimento.objects.filter(id_categoria = id_categoria)
   #lista_postres= Alimento.objects.all()
    print(lista_postres)
    return render(request,
        'menu/submenu.html',
        {'listaAlimento': lista_postres}
    )

def helados(request):
    return render(request, 'menu/submenu.html')


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
    return render(request,'login/registration.html', data)

def asignaMesa(request):
    data = {'form': MesaForm2() }
    if request.method == "POST":
        formulario = MesaForm2(data=request.POST)
        if formulario.is_valid() :
            """
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
            """
            numero_mesa = formulario.cleaned_data["numero_mesa"]
            ubicacion = formulario.cleaned_data["ubicacion"]

            encontrado =len(Mesa.objects.filter(pk=numero_mesa))
            if encontrado > 0:
                messages.error(request, "El número de mesa ya está asignada")
            else:
                mesa = Mesa(numero_mesa = numero_mesa,
                        ubicacion = ubicacion)
                algo = mesa.save()
                s["numero_mesa"] = numero_mesa
                s.create()
                print(s["numero_mesa"])
                return redirect(to="cincuentaAmigos:menuPrincipal")
        data["form"]= formulario
    return render(request,'login/asignacionMesa.html', data)



