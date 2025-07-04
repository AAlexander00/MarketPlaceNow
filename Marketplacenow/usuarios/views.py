from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ordenes.models import Orden

def register(request):
    if request.method == 'POST':
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        nombres = request.POST['nombres']

        if User.objects.filter(email=correo).exists():
            return render(request, 'register.html', {'error': 'El correo ya está registrado.'})

        user = User.objects.create_user(
            username=correo,
            email=correo,
            password=contrasena,
            first_name=nombres
        )
        user.save()
        messages.success(request, 'Cuenta creada correctamente.')
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # <- CAMBIADO
        password = request.POST.get('password')  # <- CAMBIADO
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'login.html', {'error': 'Correo o contraseña incorrectos'})

    return render(request, 'login.html')

from ordenes.models import Orden  # importa el modelo

from ordenes.models import Orden

@login_required
def perfil(request):
    ordenes = Orden.objects.filter(usuario=request.user).order_by('-fecha_creacion')

    return render(request, 'perfil.html', {
        'nombre': request.user.first_name,
        'ordenes': ordenes,
    })

def detalle(request):
    return render(request, 'detalle.html')

def direccion(request):
    return render(request, 'direccion.html')

def guardar_direccion(request):
    return render(request, 'guardar_direccion.html')