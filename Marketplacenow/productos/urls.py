from django.urls import path
from . import views

urlpatterns = [
    path('busqueda/', views.busqueda, name='busqueda'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('', views.lista_productos, name='inicio'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('<int:producto_id>/tallas/', views.obtener_tallas, name='obtener_tallas'),
    path('<int:producto_id>/colores/', views.obtener_colores, name='obtener_colores'),
    path('nuevo/', views.crear_producto, name='crear_producto'),  # ✅ Ruta protegida
]