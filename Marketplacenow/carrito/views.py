from django.shortcuts import render, redirect
from .models import CarritoItem
from productos.models import Producto
from django.contrib.auth.decorators import login_required

def carrito(request):   
    return render(request, 'carrito.html')

def favoritos(request):   
    return render(request, 'favoritos.html')

def notificaciones(request):   
    return render(request, 'notificaciones.html')

@login_required
def ver_carrito(request):
    carrito_items = CarritoItem.objects.filter(usuario=request.user)
    total = sum(item.subtotal() for item in carrito_items)
    return render(request, 'carrito/carrito.html', {'carrito_items': carrito_items, 'total': total})

@login_required
def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(ID_PRODUCTO=producto_id)
    item, created = CarritoItem.objects.get_or_create(usuario=request.user, producto=producto)
    if not created:
        item.cantidad += 1
    item.save()
    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = CarritoItem.objects.get(id=item_id, usuario=request.user)
    item.delete()
    return redirect('ver_carrito')