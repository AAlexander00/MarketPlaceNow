from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import CarritoItem
from productos.models import Producto, Talla, Color
from ordenes.models import Orden, DetalleOrden
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site


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
    try:
        producto = get_object_or_404(Producto, id=producto_id)

        # Validación de stock
        if producto.stock == 0:
            mensaje = "Este producto está agotado."
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'ok': False, 'error': mensaje}, status=400)
            return render(request, 'productos/detalle_producto.html', {
                'producto': producto,
                'tallas': producto.tallas.all(),
                'colores': producto.colores.all(),
                'error': mensaje,
            })

        if request.method == 'POST':
            cantidad = int(request.POST.get('cantidad', 1))
            talla_id = request.POST.get('talla')
            color_id = request.POST.get('color')

            # Validar cantidad mínima
            if cantidad <= 0:
                mensaje = "Debes seleccionar al menos una unidad."
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'ok': False, 'error': mensaje}, status=400)
                return render(request, 'productos/detalle_producto.html', {
                    'producto': producto,
                    'tallas': producto.tallas.all(),
                    'colores': producto.colores.all(),
                    'error': mensaje,
                })

            # Obtener talla si se envió (ya no es obligatoria)
            talla = None
            if talla_id:
                try:
                    talla = Talla.objects.get(id=talla_id)
                except:
                    talla = None  # Ignora errores de talla inválida

            # Validación de color si aplica
            color = None
            if producto.colores.exists():
                if color_id and color_id.strip():
                    color = Color.objects.get(id=color_id)
                else:
                    mensaje = "Debes seleccionar un color."
                    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                        return JsonResponse({'ok': False, 'error': mensaje}, status=400)
                    return render(request, 'productos/detalle_producto.html', {
                        'producto': producto,
                        'tallas': producto.tallas.all(),
                        'colores': producto.colores.all(),
                        'error': mensaje,
                    })

            # Buscar o crear ítem
            item, created = CarritoItem.objects.get_or_create(
                usuario=request.user,
                producto=producto,
                talla=talla,
                color=color,
                defaults={'cantidad': 0}
            )

            cantidad_total = item.cantidad + cantidad if not created else cantidad

            # Verificar stock disponible
            if cantidad_total > producto.stock:
                mensaje = f"Solo hay {producto.stock} unidades disponibles."
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'ok': False, 'error': mensaje}, status=400)
                return render(request, 'productos/detalle_producto.html', {
                    'producto': producto,
                    'tallas': producto.tallas.all(),
                    'colores': producto.colores.all(),
                    'error': mensaje,
                })

            # Guardar ítem
            item.cantidad = cantidad_total
            item.save()

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                total_items = CarritoItem.objects.filter(usuario=request.user).count()
                return JsonResponse({'ok': True, 'total_items': total_items})

        return redirect('ver_carrito')

    except Exception as e:
        import traceback
        print("🧨 ERROR en agregar_al_carrito:")
        traceback.print_exc()
        return JsonResponse({'ok': False, 'error': str(e)}, status=500)


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

        detalles = []
        for item in carrito_items:
            detalle = DetalleOrden.objects.create(
                orden=orden,
                producto=item.producto,
                cantidad=item.cantidad,
                precio_unitario=item.producto.precio,
                talla=item.talla,
                color=item.color,
            )
            detalles.append(detalle)

        # Eliminamos carrito
        carrito_items.delete()

        # ✅ Enviar correo con la factura
        dominio = get_current_site(request).domain
        detalles_orden = orden.detalles.select_related('producto', 'talla', 'color')

        html_content = render_to_string("factura_email.html", {
            'orden': orden,
            'detalles': detalles_orden,
            'dominio': dominio,
            'usuario': request.user
        })
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            subject="🧾 Tu factura de MarketPlaceNow",
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[request.user.email],
        )
        email.attach_alternative(html_content, "text/html")
        email.send()

        return redirect('confirmacion_pago')

    return redirect('ver_carrito')


def contar_items_carrito(usuario):
    return CarritoItem.objects.filter(usuario=usuario).count()