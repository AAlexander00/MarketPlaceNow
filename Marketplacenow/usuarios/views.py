from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from datetime import date
from ordenes.models import Orden
from .models import PerfilUsuario, Direccion

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('perfil')
        else:
            return render(request, 'login.html', {'error': 'Correo o contraseña incorrectos'})

    return render(request, 'login.html')


@login_required
def perfil(request):
    ordenes = Orden.objects.filter(usuario=request.user).order_by('-fecha_creacion')

    return render(request, 'perfil.html', {
        'nombre': request.user.first_name,
        'apellido': request.user.last_name,
        'ordenes': ordenes,
    })


from datetime import date
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import PerfilUsuario  # asegúrate de tener este import correcto

@login_required
def detalle(request):
    user = request.user

    # Si no hay perfil, no lo creamos aún (esperamos a POST con datos válidos)
    perfil = PerfilUsuario.objects.filter(user=user).first()

    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        genero = request.POST.get('titulo')
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')
        actual = request.POST.get('password_actual')
        nueva = request.POST.get('nueva_password')
        confirmar = request.POST.get('confirmar_password')

        errores = []
        fecha_nac = None

        if not nombre or not apellido:
            errores.append("El nombre y apellido son obligatorios.")

        try:
            fecha_nac = date(int(anio), int(mes), int(dia))
            hoy = date.today()
            edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
            if edad < 18:
                errores.append("Debes tener 18 años o más.")
        except:
            errores.append("Fecha de nacimiento inválida.")

        if actual or nueva or confirmar:
            if not user.check_password(actual):
                errores.append("La contraseña actual es incorrecta.")
            elif not nueva or not confirmar:
                errores.append("Debes ingresar y confirmar la nueva contraseña.")
            elif nueva != confirmar:
                errores.append("La nueva contraseña no coincide.")

        if errores:
            for e in errores:
                messages.error(request, e)
        else:
            user.first_name = nombre
            user.last_name = apellido
            user.save()

            if not perfil:
                perfil = PerfilUsuario.objects.create(
                    user=user,
                    genero=genero,
                    fecha_nacimiento=fecha_nac
                )
            else:
                perfil.genero = genero
                perfil.fecha_nacimiento = fecha_nac
                perfil.save()

            if actual and nueva == confirmar:
                user.set_password(nueva)
                user.save()
                update_session_auth_hash(request, user)

            messages.success(request, "✅ Datos actualizados correctamente.")
            return redirect('detalle')

    # Datos existentes (si perfil no existe aún, evitamos errores)
    fecha = perfil.fecha_nacimiento if perfil and perfil.fecha_nacimiento else None

    contexto = {
        'nombre': user.first_name,
        'apellido': user.last_name,
        'genero': perfil.genero if perfil else '',
        'fecha_nacimiento': fecha,
        'dia_actual': fecha.day if fecha else '',
        'mes_actual': fecha.month if fecha else '',
        'anio_actual': fecha.year if fecha else '',
        'dias': range(1, 32),
        'meses': range(1, 13),
        'anios': range(1950, date.today().year + 1),
    }

    return render(request, 'detalle.html', contexto)


@login_required
def direccion(request):
    try:
        direccion = Direccion.objects.get(usuario=request.user)
    except Direccion.DoesNotExist:
        direccion = None

    return render(request, 'direccion.html', {
        'direccion': direccion
    })

@login_required
def guardar_direccion(request):
    try:
        direccion = Direccion.objects.get(usuario=request.user)
    except Direccion.DoesNotExist:
        direccion = None

    if request.method == 'POST':
        data = {
            'direccion': request.POST.get('direccion'),
            'ciudad': request.POST.get('ciudad'),
            'departamento': request.POST.get('departamento'),
            'codigo_postal': request.POST.get('codigo_postal'),
            'telefono': request.POST.get('telefono'),
        }

        if direccion:
            for campo, valor in data.items():
                setattr(direccion, campo, valor)
        else:
            direccion = Direccion(usuario=request.user, **data)

        direccion.save()
        messages.success(request, "✅ Dirección guardada correctamente.")
        return redirect('direccion')

    return render(request, 'guardar_direccion.html', {
        'direccion': direccion
    })