from django.shortcuts import render, redirect
from .models import Usuario
from django.utils import timezone
import datetime
import random

def olvide_contrasena(request):
    return render(request, 'olvide_contrasena.html')

def register(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        nombres = request.POST['nombres']

        # Validación simple
        if Usuario.objects.filter(correoe=correo).exists():
            return render(request, 'register.html', {'error': 'El correo ya está registrado.'})

        usuario = Usuario(
            id_carrito=1,
            nombres_usuario=nombres,
            correoe=correo,
            contrasena=contrasena,
            direccion='',
            telefono=0,
            fecharegistro=timezone.now().date(),
            token='',
            token_expira=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        usuario.save()
        return redirect('login')  # nombre de la URL del login

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']

        try:
            usuario = Usuario.objects.get(correoe=correo, contrasena=contrasena)
            request.session['usuario_id'] = usuario.id_usuario
            request.session['usuario_nombre'] = usuario.nombres_usuario
            return redirect('perfil')  # redirige a perfil.html
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'Correo o contraseña incorrectos'})

    return render(request, 'login.html')

def perfil(request):
    if 'usuario_id' not in request.session:
        return redirect('login')

    return render(request, 'perfil.html', {
        'nombre': request.session['usuario_nombre']
    })
