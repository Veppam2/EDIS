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
    return asignaMesa(request)

def menuPrincipal(request):
    listaCategorias = Categoria.objects.all()
    print("menuprincipal")
    return render(request,
        'menu/menuPrincipal.html',
        {'listaCategorias': listaCategorias}
    )

def entradas(request):
    id_categoria = Categoria.objects.get(nombre = "Entradas")
    lista_entradas= Alimento.objects.filter(id_categoria = id_categoria)
    print(lista_entradas)
    return render(request,
        'menu/menuEntradas.html',
        {'listaEntradas': lista_entradas}
    )

def platillos(request):
    id_categoria = Categoria.objects.get(nombre = "Platillos principales")
    lista_platillos= Alimento.objects.filter(id_categoria = id_categoria)
    print(lista_platillos)
    return render(request,
        'menu/menuPlatillos.html',
        {'listaPlatillos': lista_platillos}
    )

def bebidas(request):
    id_categoria = Categoria.objects.get(nombre = "Bebidas")
    lista_bebidas= Alimento.objects.filter(id_categoria = id_categoria)
    print(lista_bebidas)
    return render(request,
        'menu/menuBebidas.html',
        {'listaBebidas': lista_bebidas}
    )

def postres(request):
    id_categoria = Categoria.objects.get(nombre = "Postres")
    lista_postres= Alimento.objects.filter(id_categoria = id_categoria)
    print(lista_postres)
    return render(request,
        'menu/menuPostres.html',
        {'listaPostres': lista_postres}
    )


def helados(request):
    return render(request, 'menu/menuS.html')


def asignaMesa(request):
    if request.method == "POST":
        numero_mesa = request.POST.get("numero_mesa")
        ubicacion = request.POST.get("ubicacion")

        if not numero_mesa:
            messages.error(request, "Debes seleccionar una mesa.")

        elif not ubicacion:
            messages.error(request, "Debes seleccionar una ubicación.")

        # Verificar si el número de mesa ya está asignado
        elif Mesa.objects.filter(numero_mesa=numero_mesa).exists():
            messages.error(request, "La mesa seleccionada ya está ocupada.")

        else:
            # Crear una nueva instancia de la mesa y guardarla en la base de datos
            mesa = Mesa(numero_mesa=numero_mesa, ubicacion=ubicacion)
            mesa.save()
            s["numero_mesa"] = numero_mesa
            s.create()
            print(s["numero_mesa"])
            # Redireccionar al menú principal u otra página relevante
            return redirect(to="cincuentaAmigos:menuPrincipal")

    return render(request, 'index.html')    


def agregar_al_carrito(request, alimento_id, cantidad):
    print(s["numero_mesa"])
    if request.method == 'POST':
        mesa = Mesa.objects.get(numero_mesa = s["numero_mesa"])
        alimento = Alimento.objects.get(id_alimento = alimento_id)

        for _ in range(cantidad):
            carrito = Carrito(numero_mesa=mesa, id_alimento=alimento)
            carrito.save()

        return redirect(request.META['HTTP_REFERER'])

    return redirect(to="cincuentaAmigos:menuPrincipal")



