from .models import CarritoItem

def contador_carrito(request):
    if request.user.is_authenticated:
        total = CarritoItem.objects.filter(usuario=request.user).count()
    else:
        total = 0
    return {
        'total_items_carrito': total
    }