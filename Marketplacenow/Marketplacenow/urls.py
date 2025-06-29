from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitio.urls')),  # página principal
    path('usuarios/', include('usuarios.urls')),
    path('carrito/', include('carrito.urls')),
    path('productos/', include('productos.urls')),
    path('ordenes/', include('ordenes.urls')),
    path('pagos/', include('pagos.urls')),
]

# Rutas para recuperación de contraseña
urlpatterns += [
    path('recuperar/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name="usuarios/password_reset_done.html"
    ), name="password_reset_done"),

    path('recuperar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),

    path('recuperar/completo/', auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
]

# Archivos estáticos y media solo en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)