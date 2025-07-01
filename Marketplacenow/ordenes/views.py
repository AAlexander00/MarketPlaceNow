from django.shortcuts import render, redirect, get_object_or_404, redirect
from ordenes.models import Orden, DetalleOrden
from productos.models import Producto, Talla, Color
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
    producto = get_object_or_404(Producto, id=producto_id)

    if producto.stock == 0:
        return render(request, 'detalle_producto.html', {
            'producto': producto,
            'tallas': producto.tallas.all(),
            'colores': producto.colores.all(),
            'error': "Este producto está agotado.",
        })

    if request.method == 'POST':
        try:
            cantidad = int(request.POST.get('cantidad', 1))
            talla_id = request.POST.get('talla')
            color_id = request.POST.get('color')

            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a 0.")

            talla = None
            if talla_id:
                talla = Talla.objects.get(id=talla_id)

            color = None
            if color_id:
                color = Color.objects.get(id=color_id)

            if cantidad > producto.stock:
                return render(request, 'detalle_producto.html', {
                    'producto': producto,
                    'tallas': producto.tallas.all(),
                    'colores': producto.colores.all(),
                    'error': f"Solo hay {producto.stock} unidades disponibles.",
                })

            orden = Orden.objects.create(
                usuario=request.user,
                total=producto.precio * cantidad,
                estado='pendiente'
            )

            DetalleOrden.objects.create(
                orden=orden,
                producto=producto,
                cantidad=cantidad,
                talla=talla,
                color=color,
                precio_unitario=producto.precio
            )

            messages.success(request, 'Orden creada correctamente.')
            return redirect('detalle_orden', orden.id)

        except Exception as e:
            return render(request, 'detalle_producto.html', {
                'producto': producto,
                'tallas': producto.tallas.all(),
                'colores': producto.colores.all(),
                'error': str(e),
            })

    return redirect('detalle_producto', producto_id=producto.id)