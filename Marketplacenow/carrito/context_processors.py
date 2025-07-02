from carrito.models import CarritoItem
from productos.models import Favorito

def contadores_generales(request):
    total_items_carrito = 0
    total_favoritos = 0

    if request.user.is_authenticated:
        total_items_carrito = CarritoItem.objects.filter(usuario=request.user).count()
        total_favoritos = Favorito.objects.filter(usuario=request.user).count()

    return {
        'total_items_carrito': total_items_carrito,
        'total_favoritos': total_favoritos
    }