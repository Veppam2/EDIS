from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from django.core.exceptions import ObjectDoesNotExist

from ..models import *

# Autor: EDIS
# Vistas de Login

def sesion_mesa(request):
    """
    Obtiene el número de mesa de la sesión.
    """
    return request.session.get('numero_mesa')


def admin_login(request):
    """
    Redirige a la página de administración.
    """
    return redirect('/admin')


def index(request):
    """
    Página de inicio.
    """
    val = sesion_mesa(request)
    if val is None:
        return asigna_mesa(request)
    else:
        return redirect(to="cincuentaAmigos:menu-principal")


def logout(request):
    """
    Cierra la sesión y elimina la mesa.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    mesa.delete()
    request.session.flush()
    return redirect('/')


def asigna_mesa(request):
    """
    Asigna una mesa al realizar una solicitud POST.
    """
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
    """
    Página del menú principal.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    listaCategorias = Categoria.objects.all()
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request,
        'menu/menu-principal.html',
        {'listaCategorias': listaCategorias, 
         'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )

# Vistas del Carrito

def agregar_al_carrito(request):
    """
    Agrega un elemento al carrito.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
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
    """
    Elimina el carrito de la mesa actual y redirige según la ubicación.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    ubicacion = str(request.POST.get("ubicacion"))
    lista_carrito = Carrito.objects.filter(numero_mesa = mesa)
    lista_carrito.delete()

    if(ubicacion == 'Votacion'):
        return redirect(to="cincuentaAmigos:votacion")
    
    elif(ubicacion == 'Menu'):
        return redirect(to="cincuentaAmigos:menu-principal")

    return redirect(request.META['HTTP_REFERER'])


def eliminar_alimento(request):
    """
    Elimina un elemento del carrito.
    """
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    alimento_id = int(request.POST.get("alimento_id"))
    alimento = Alimento.objects.get(id_alimento=alimento_id)
    
    try:
        carrito = Carrito.objects.get(numero_mesa=mesa, id_alimento=alimento)
        carrito.delete()
            
    except Carrito.DoesNotExist:
        raise ObjectDoesNotExist("El elemento no existe en el carrito.")

    return redirect(request.META['HTTP_REFERER'])


def eliminar_cantidad(request):
    """
    Elimina una cantidad de un elemento del carrito.
    """
    mesa = Mesa.objects.get(numero_mesa = sesion_mesa(request))
    cantidad = int(request.POST.get("cantidad"))
    alimento_id = int(request.POST.get("alimento_id"))
    alimento = Alimento.objects.get(id_alimento=alimento_id)
    
    try:
        carrito = Carrito.objects.get(numero_mesa=mesa, id_alimento=alimento)
        
        if carrito.cantidad == 1:
            carrito.delete()
        
        else:
            carrito.cantidad -= cantidad
            carrito.save()
            
    except Carrito.DoesNotExist:
        raise ObjectDoesNotExist("El elemento no existe en el carrito.")

    return redirect(request.META['HTTP_REFERER'])


def obtener_datos_carrito(request):
    """
    Obtiene los datos del carrito de la sesión actual.
    Retorna una lista de los alimentos en el carrito con su cantidad y precio total,
    así como el precio total de todos los alimentos en el carrito.
    """
    mesa = Mesa.objects.get(numero_mesa=sesion_mesa(request))
    lista_carrito = Carrito.objects.filter(numero_mesa=mesa)

    precio_total = 0

    # Calcular el precio total del alimento y la cantidad para cada elemento en el carrito
    datos_carrito = []
    for item in lista_carrito:
        alimento = item.id_alimento
        precio = alimento.precio * item.cantidad
        datos_carrito.append({
            'alimento': alimento,
            'cantidad': item.cantidad,
            'precio': precio
        })
        precio_total += precio

    return datos_carrito, precio_total

# Votación de helados

def nuevo_comensal(request):
    """
    Elimina el carrito y los votos de la sesión actual y redirige al menú principal.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")
    carrito = Carrito.objects.filter(numero_mesa = sesion_mesa(request))
    votacion = Votacion.objects.filter(numero_mesa = sesion_mesa(request))
    carrito.delete()
    votacion.delete()
    return menu_principal(request)


def votacion_helados(request):
    """
    Realiza la votación de helados.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    lista_helados= Helado.objects.all()
    datos_carrito, precio_total = obtener_datos_carrito(request)
    
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
         'votos': None,
         'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )


def helados(request):
    """
    Muestra el menú de helados y realiza la votación si ya hay votos registrados.
    """
    val = sesion_mesa(request)
    if val is None:
        return redirect(to="cincuentaAmigos:index")

    if Votacion.objects.filter(numero_mesa = sesion_mesa(request)).exists():
        return votacion_helados(request)
    lista_helados= Helado.objects.all()
    datos_carrito, precio_total = obtener_datos_carrito(request)
    return render(request,
        'helados/menu-helado.html',
        {'listaHelado': lista_helados, 
         'datosCarrito': datos_carrito,
         'precioTotal': precio_total}
    )
