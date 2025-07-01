from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Producto, Talla, Color, Marca, Categoria

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