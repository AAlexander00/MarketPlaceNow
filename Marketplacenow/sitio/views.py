from django.shortcuts import render
from productos.models import Producto

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos,
    'es_inicio': True,
    })

def sobre(request):
    return render(request, 'sobre.html')

def contacto(request):
    return render(request, 'contacto.html')

def terminos(request):
    return render(request, 'terminos.html')

def privacidad(request):
    return render(request, 'privacidad.html')