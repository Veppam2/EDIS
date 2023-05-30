from django.shortcuts import render

from ..models import Categoria, Alimento
from .views import *


def entradas(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    id_categoria = Categoria.objects.get(nombre="Entradas")
    lista_entradas = Alimento.objects.filter(id_categoria=id_categoria)
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request, 
                  'menu/menu-entradas.html', 
                  {'listaEntradas': lista_entradas, 
                   'datosCarrito': datos_carrito,
                   'precioTotal': precio_total}
    )


def platillos(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    id_categoria = Categoria.objects.get(nombre = "Platillos principales")
    lista_platillos= Alimento.objects.filter(id_categoria = id_categoria)
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request,
        'menu/menu-platillos.html',
        {'listaPlatillos': lista_platillos,
         'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )


def bebidas(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    id_categoria = Categoria.objects.get(nombre = "Bebidas")
    lista_bebidas= Alimento.objects.filter(id_categoria = id_categoria)
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request,
        'menu/menu-bebidas.html',
        {'listaBebidas': lista_bebidas, 
         'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )


def postres(request):
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    id_categoria = Categoria.objects.get(nombre = "Postres")
    lista_postres= Alimento.objects.filter(id_categoria = id_categoria)
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request,
        'menu/menu-postres.html',
        {'listaPostres': lista_postres, 
         'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )


def carrito(request):
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request,
        'carrito/carrito.html',
        {'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )
