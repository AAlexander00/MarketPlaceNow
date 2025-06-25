from django.shortcuts import render, get_object_or_404, redirect
from ordenes.models import Orden
from productos.models import Producto
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Orden, DetalleOrden
from django.contrib import messages

@login_required
def detalle_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)
    return render(request, 'ordenes/detalle_orden.html', {'orden': orden})

@login_required
def pagar_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)

    if request.method == 'POST':
        orden.estado = 'pagado'
        orden.fecha_creacion = timezone.now()  # o puedes agregar campo fecha_pago si lo deseas
        orden.save()
        messages.success(request, '¡Pago realizado con éxito!')
        return redirect('detalle_orden', orden_id=orden.id)

    return redirect('detalle_orden', orden_id=orden.id)

@login_required
def ordenar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    orden = Orden.objects.create(
        usuario=request.user,
        total=producto.PRECIO,
        estado='pendiente'  # Se marca como pagado al presionar el botón
    )

    DetalleOrden.objects.create(
        orden=orden,
        producto=producto,
        cantidad=1,
        precio_unitario=producto.PRECIO
    )

    messages.success(request, 'Orden creada. Puedes proceder al pago.')
    return redirect('detalle_orden', orden.id)