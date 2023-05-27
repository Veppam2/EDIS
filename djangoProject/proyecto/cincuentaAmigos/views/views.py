from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sessions.backends.db import SessionStore

from ..models import *

s = SessionStore()

# Vistas de Login

def adminLogin(request):
    return redirect('/admin')


def index(request):
    return asignaMesa(request)


def asignaMesa(request):
    if request.method == "POST":
        numero_mesa = request.POST.get("numero-mesa")
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
            s["numero-mesa"] = numero_mesa
            s.create()
            
            return redirect(to="cincuentaAmigos:menu-principal")

    return render(request, 'index.html')    


def menu_principal(request):
    listaCategorias = Categoria.objects.all()
    lista_carrito = mostrar_carrito(request)
    return render(request,
        'menu/menu-principal.html',
        {'listaCategorias': listaCategorias, 'listaCarrito': lista_carrito}
    )

# Vistas del Carrito

def mostrar_carrito(request):
    mesa = Mesa.objects.get(numero_mesa = s["numero-mesa"])
    lista_carrito = Carrito.objects.filter(numero_mesa = mesa)
    lista_alimentos = []
    for item in lista_carrito:
        alimento = Alimento.objects.get(id_alimento=item.id_alimento_id)
        lista_alimentos.append(alimento)

    return lista_alimentos


def agregar_al_carrito(request):
    if request.method == 'POST':
        mesa = Mesa.objects.get(numero_mesa = s["numero-mesa"])
        cantidad = int(request.POST.get("cantidad"))
        alimento_id = int(request.POST.get("cartItemId"))
        alimento = Alimento.objects.get(id_alimento = alimento_id)

        for _ in range(cantidad):
            carrito = Carrito(numero_mesa=mesa, id_alimento=alimento)
            carrito.save()

        return redirect(request.META['HTTP_REFERER'])

    return redirect(to="cincuentaAmigos:menuPrincipal")


def eliminar_carrito(request):
    mesa = Mesa.objects.get(numero_mesa = s["numero-mesa"])
    lista_carrito = Carrito.objects.filter(numero_mesa = mesa)
    
    lista_carrito.delete()

    return redirect(request.META['HTTP_REFERER'])


