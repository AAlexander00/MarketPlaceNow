from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ordenes.models import Orden
from django.contrib import messages
from django.utils import timezone

@login_required
def pagar_orden(request, orden_id):
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)

    if request.method == 'POST':
        orden.estado = 'pagado'
        orden.save()
        messages.success(request, "¡Pago realizado con éxito!")
        return redirect('confirmacion_pago')  # Cambiado aquí

    return render(request, 'pagos/realizar_pago.html', {'orden': orden})

@login_required
def confirmacion_pago(request):
    return render(request, 'pagos/confirmacion_pago.html')