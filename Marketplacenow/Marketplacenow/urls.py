from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from productos import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sitio.urls')), 
    path('', include('usuarios.urls')),
    path('', include('carrito.urls')),
    path('', include('productos.urls')),
    path('', views.lista_productos, name='inicio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)