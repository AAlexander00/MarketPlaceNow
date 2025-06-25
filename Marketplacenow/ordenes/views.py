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
        orden.pagado = True
        orden.fecha_pago = timezone.now()
        orden.save()
        return redirect('perfil')  # Redirige a perfil u otra vista de confirmación
    
    return redirect('detalle_orden', orden_id=orden.id)

@login_required
def ordenar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    # Crear la orden
    orden = Orden.objects.create(
        usuario=request.user,
        total=producto.PRECIO,
        estado='pagado'
    )

    # Crear detalle de la orden
    DetalleOrden.objects.create(
        orden=orden,
        producto=producto,
        cantidad=1,
        precio_unitario=producto.PRECIO
    )

    messages.success(request, 'Compra realizada con éxito.')
    return redirect('detalle_orden', orden.id)