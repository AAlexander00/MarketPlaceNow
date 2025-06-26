from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CarritoItem
from productos.models import Producto
from ordenes.models import Orden, DetalleOrden


def favoritos(request):   
    return render(request, 'carrito/favoritos.html')

def notificaciones(request):   
    return render(request, 'carrito/notificaciones.html')

def carrito(request):
    return render(request, 'carrito/carrito.html')

@login_required
def ver_carrito(request):
    carrito_items = CarritoItem.objects.filter(usuario=request.user)
    total = sum(item.subtotal() for item in carrito_items)
    total_items_carrito = contar_items_carrito(request.user)
    return render(request, 'carrito/carrito.html', {
        'carrito_items': carrito_items,
        'total': total,
        'total_items_carrito': total_items_carrito
    })

@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, ID_PRODUCTO=producto_id)
    item, created = CarritoItem.objects.get_or_create(usuario=request.user, producto=producto)
    if not created:
        item.cantidad += 1
    item.save()

    total_items = CarritoItem.objects.filter(usuario=request.user).count()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'ok': True, 'total_items': total_items})

    return redirect('ver_carrito')

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, usuario=request.user)
    item.delete()
    return redirect('ver_carrito')


@login_required
def seleccionar_pago(request):
    carrito_items = CarritoItem.objects.filter(usuario=request.user)
    total = sum(item.subtotal() for item in carrito_items)

    if not carrito_items.exists():
        return redirect('ver_carrito')

    return render(request, 'carrito/seleccionar_pago.html', {
        'total': total
    })


@login_required
def procesar_pago(request):
    if request.method == 'POST':
        carrito_items = CarritoItem.objects.filter(usuario=request.user)
        if not carrito_items.exists():
            return redirect('ver_carrito')

        orden = Orden.objects.create(
            usuario=request.user,
            total=sum(item.subtotal() for item in carrito_items),
            estado='pagado'
        )

        for item in carrito_items:
            DetalleOrden.objects.create(
                orden=orden,
                producto=item.producto,
                cantidad=item.cantidad,
                precio_unitario=item.producto.PRECIO
            )

        carrito_items.delete()
        return redirect('confirmacion_pago')

    return redirect('ver_carrito')


def contar_items_carrito(usuario):
    return CarritoItem.objects.filter(usuario=usuario).count()