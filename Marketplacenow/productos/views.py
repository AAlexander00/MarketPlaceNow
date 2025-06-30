from productos.models import Producto
from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.db.models import Q
from django.http import JsonResponse

def busqueda(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        resultados = Producto.objects.filter(
            Q(NOMBRE_PRODUCTO__icontains=query) | 
            Q(DESCRIPCION__icontains=query)
        )

    return render(request, 'productos/busqueda.html', {
        'query': query,
        'resultados': resultados
    })

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/productos.html', {'productos': productos})


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    tallas = producto.tallas.all()
    colores = producto.colores.all()

    relacionados = Producto.objects.filter(
        categoria=producto.categoria
    ).exclude(id=producto.id)[:4]

    return render(request, 'productos/detalle_producto.html', {
        'producto': producto,
        'tallas': tallas,
        'colores': colores,
        'relacionados': relacionados,
    })

def obtener_tallas(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    tallas = producto.tallas.all()
    data = {
        'tallas': [{'id': t.id, 'valor': t.VALOR_TALLA} for t in tallas]
    }
    return JsonResponse(data)

def obtener_colores(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    colores = producto.colores.all()
    data = {
        'colores': [{'id': c.id, 'nombre': c.nombre} for c in colores]
    }
    return JsonResponse(data)