from django.shortcuts import render, get_object_or_404, redirect
from ordenes.models import Orden
from productos.models import Producto
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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