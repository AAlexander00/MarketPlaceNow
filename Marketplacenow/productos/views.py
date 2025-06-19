from django.shortcuts import render
from productos.models import Producto

def busqueda(request):
    return render(request, 'busqueda.html')

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})