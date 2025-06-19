from django.shortcuts import render

def carrito(request):   
    return render(request, 'carrito.html')

def favoritos(request):   
    return render(request, 'favoritos.html')

def notificaciones(request):   
    return render(request, 'notificaciones.html')