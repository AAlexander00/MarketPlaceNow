from productos.models import Producto
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Talla, Color, Marca, Categoria
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages

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


@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        descripcion = request.POST.get('descripcion', '').strip()
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')
        tallas_ids = request.POST.getlist('tallas')
        colores_ids = request.POST.getlist('colores')
        marcas_ids = request.POST.getlist('marcas')
        imagen = request.FILES.get('imagen')

        errores = []

        if not nombre:
            errores.append("El nombre del producto es obligatorio.")
        if not precio or not precio.replace('.', '', 1).isdigit() or float(precio) <= 0:
            errores.append("El precio debe ser un número positivo.")
        if not stock or not stock.isdigit() or int(stock) < 0:
            errores.append("El stock debe ser un número entero positivo.")
        if not categoria_id:
            errores.append("Debe seleccionar una categoría.")

        if errores:
            categorias = Categoria.objects.all()
            tallas = Talla.objects.all()
            colores = Color.objects.all()
            marcas = Marca.objects.all()
            return render(request, 'productos/crear_producto.html', {
                'errores': errores,
                'categorias': categorias,
                'tallas': tallas,
                'colores': colores,
                'marcas': marcas,
            })

        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria_id=categoria_id,
            publicado_por=request.user,
            imagen=imagen
        )

        if tallas_ids:
            producto.tallas.set(tallas_ids)
        if colores_ids:
            producto.colores.set(colores_ids)
        if marcas_ids:
            producto.marcas.set(marcas_ids)

        producto.save()
        messages.success(request, 'Producto creado correctamente.')
        return redirect('detalle_producto', producto_id=producto.id)

    categorias = Categoria.objects.all()
    tallas = Talla.objects.all()
    colores = Color.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'productos/crear_producto.html', {
        'categorias': categorias,
        'tallas': tallas,
        'colores': colores,
        'marcas': marcas,
    })