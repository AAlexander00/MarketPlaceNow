from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from productos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de tus apps
    path('', include('sitio.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('carrito/', include('carrito.urls')),
    path('productos/', include('productos.urls')),

    # Página principal muestra productos
    path('', views.lista_productos, name='inicio'),
]

# Archivos estáticos y multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)