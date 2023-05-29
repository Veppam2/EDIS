from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count

from ..models import *

# Vistas de Login

def sesion_mesa(request):
    return request.session.get('numero_mesa');


def admin_login(request):
    return redirect('/admin')


def index(request):
    return asigna_mesa(request)


def logout(request):
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    mesa.delete()
    request.session.flush()
    return redirect('/')


def asigna_mesa(request):
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
            request.session['numero_mesa'] = numero_mesa
            
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
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    lista_carrito = Carrito.objects.filter(numero_mesa = mesa)
    lista_alimentos = []
    for item in lista_carrito:
        alimento = Alimento.objects.get(id_alimento=item.id_alimento_id)
        lista_alimentos.append(alimento)

    return lista_alimentos


def agregar_al_carrito(request):
    if request.method == 'POST':
        mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
        cantidad = int(request.POST.get("cantidad"))
        alimento_id = int(request.POST.get("cartItemId"))
        alimento = Alimento.objects.get(id_alimento=alimento_id)

        try:
            # Buscar el elemento en el carrito
            carrito = Carrito.objects.get(numero_mesa=mesa, id_alimento=alimento)
            # Incrementar la cantidad en la cantidad especificada
            carrito.cantidad += cantidad
            carrito.save()
        except Carrito.DoesNotExist:
            # Si el elemento no está en el carrito, agregarlo con la cantidad especificada
            carrito = Carrito(numero_mesa=mesa, id_alimento=alimento, cantidad=cantidad)
            carrito.save()

        return redirect(request.META['HTTP_REFERER'])

    return redirect(to="cincuentaAmigos:menu-principal")


def eliminar_carrito(request):
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    lista_carrito = Carrito.objects.filter(numero_mesa = mesa)
    
    lista_carrito.delete()

    return redirect(request.META['HTTP_REFERER'])

# Votación de helados

def nuevo_comensal(request):
    carrito = Carrito.objects.filter(numero_mesa = sesion_mesa(request))
    votacion = Votacion.objects.filter(numero_mesa = sesion_mesa(request))
    carrito.delete()
    votacion.delete()
    return menu_principal(request)


def votacion_helados(request):
    lista_helados= Helado.objects.all()
    
    if request.method == "POST":
        mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
        votante = request.POST.get("nombre_votante")
        sabor_votado = request.POST.get("sabor_votado")
        helado = Helado.objects.get(sabor = sabor_votado)
        nuevo_voto = Votacion( numero_mesa=mesa,
                              id_helado=helado,
                              nombre_votante = votante )
        nuevo_voto.save()
        votos = Votacion.objects.filter(numero_mesa = sesion_mesa(request)).values('id_helado__sabor').annotate(num_votos=Count('id_helado')).order_by('-num_votos')
        return render(request,
            'helados/votacion-helados.html',
            {'listaHelado': lista_helados,
             'votos': votos})
    return render(request,
        'helados/votacion-helados.html',
        {'listaHelado': lista_helados,
         'votos': None}
    )


def helados(request):
    if Votacion.objects.filter(numero_mesa = sesion_mesa(request)).exists():
        return votacion_helados(request)
    lista_helados= Helado.objects.all()
    lista_carrito = mostrar_carrito(request)
    return render(request,
        'helados/menu-helado.html',
        {'listaHelado': lista_helados, 'listaCarrito': lista_carrito}
    )