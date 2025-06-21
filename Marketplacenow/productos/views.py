from django.shortcuts import render
from productos.models import Producto
from django.shortcuts import render, get_object_or_404
from .models import Producto

def busqueda(request):
    return render(request, 'busqueda.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, ID_PRODUCTO=producto_id)

    # Suponiendo que hay un campo ID_CATEGORIA
    relacionados = Producto.objects.filter(ID_CATEGORIA=producto.ID_CATEGORIA).exclude(ID_PRODUCTO=producto_id)[:4]

    return render(request, 'productos/detalle_producto.html', {
        'producto': producto,
        'relacionados': relacionados,
    })