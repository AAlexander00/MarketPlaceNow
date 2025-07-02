from productos.models import Producto
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Talla, Color, Marca, Categoria
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from .models import Favorito
from django.urls import reverse

def busqueda(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        resultados = Producto.objects.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query)
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
        colores_ids = [c for c in request.POST.getlist('colores') if c.strip()]
        marca_id = request.POST.get('marca')
        imagen = request.FILES.get('imagen')

        # ✅ Depuración (tallas que el usuario supuestamente selecciona)
        tallas_ids = request.POST.getlist('tallas')
        print("✅ Tallas recibidas del formulario:", tallas_ids)

        errores = []

        # Validaciones principales
        if not nombre:
            errores.append("El nombre del producto es obligatorio.")
        try:
            precio = float(precio)
            if precio <= 0:
                errores.append("El precio debe ser un número positivo.")
        except:
            errores.append("El precio debe ser un número válido.")

        try:
            stock = int(stock)
            if stock < 0:
                errores.append("El stock debe ser un número entero positivo.")
        except:
            errores.append("El stock debe ser un número entero válido.")

        categoria_obj = Categoria.objects.first()
        if not categoria_obj:
            errores.append("⚠️ No hay categorías registradas en el sistema.")

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
                'tallas_seleccionadas': tallas_ids,
                'colores_seleccionados': colores_ids,
                'marca_seleccionada': marca_id,
                'categoria_seleccionada': categoria_id,
                'request': request,
            })

        # Crear producto
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            categoria=categoria_obj,
            publicado_por=request.user,
            imagen=imagen
        )

        # ✅ Plan de emergencia: asignar tallas S, M, L y XL por defecto
        tallas_predeterminadas = Talla.objects.filter(VALOR_TALLA__in=["S", "M", "L", "XL"])
        producto.tallas.set(tallas_predeterminadas)

        # Colores y marcas (reales del formulario)
        if colores_ids:
            producto.colores.set(colores_ids)
        if marca_id:
            producto.marcas.set([marca_id])

        producto.save()
        messages.success(request, '✅ Producto creado correctamente.')
        return redirect('detalle_producto', producto_id=producto.id)

    # GET
    categorias = Categoria.objects.all()
    tallas = Talla.objects.all()
    colores = Color.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'productos/crear_producto.html', {
        'categorias': categorias,
        'tallas': tallas,
        'colores': colores,
        'marcas': marcas,
        'tallas_seleccionadas': [],
        'colores_seleccionados': [],
        'marca_seleccionada': '',
        'categoria_seleccionada': '',
        'request': request,
    })


@login_required
def toggle_favorito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    favorito, creado = Favorito.objects.get_or_create(usuario=request.user, producto=producto)

    if not creado:
        favorito.delete()
        messages.info(request, f'❌ Producto eliminado de favoritos.')
    else:
        messages.success(request, f'✅ Producto agregado a favoritos.')

    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect(reverse('detalle_producto', args=[producto.id]))


@login_required
def ver_favoritos(request):
    favoritos = Favorito.objects.filter(usuario=request.user).select_related('producto')
    productos = [f.producto for f in favoritos]
    return render(request, 'productos/favoritos.html', {
        'favoritos': productos
    })


def ofertas(request):
    return render(request, 'productos/ofertas.html',)
def nuevo(request):
    return render(request, 'productos/nuevo.html',)

def telefono(request):
    return render(request, 'productos/telefono.html')
def computador(request):
    return render(request, 'productos/computador.html')
def accesorios(request):
    return render(request, 'productos/accesorios.html')
def hombres(request):
    return render(request, 'productos/hombres.html')
def mujeres(request):
    return render(request, 'productos/mujeres.html')
def ninos(request):
    return render(request, 'productos/ninos.html')
def joyas(request):
    return render(request, 'productos/joyas.html')
def calzado(request):
    return render(request, 'productos/calzado.html')
def muebles(request):
    return render(request, 'productos/muebles.html')
def exterior(request):
    return render(request, 'productos/exterior.html')
def interior(request):
    return render(request, 'productos/interior.html')
def decoracion(request):
    return render(request, 'productos/decoracion.html')
def jardineria(request):
    return render(request, 'productos/jardineria.html')
def ficcion(request):
    return render(request, 'productos/ficcion.html')
def romance(request):
    return render(request, 'productos/romance.html')
def infantiles(request):
    return render(request, 'productos/infantiles.html')