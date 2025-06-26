from django.shortcuts import render
from productos.models import Producto
from carrito.models import CarritoItem

def inicio(request):
    productos = Producto.objects.all()
    total_items_carrito = 0

    if request.user.is_authenticated:
        total_items_carrito = contar_items_carrito(request.user)

    return render(request, 'sitio/inicio.html', {
        'es_inicio': True,
        'productos': productos,  # <- necesario para mostrar productos
        'total_items_carrito': total_items_carrito
    })

def contar_items_carrito(usuario):
    return CarritoItem.objects.filter(usuario=usuario).count()

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    return render(request, 'contacto.html')

def terminos(request):
    return render(request, 'terminos.html')

def privacidad(request):
    return render(request, 'privacidad.html')