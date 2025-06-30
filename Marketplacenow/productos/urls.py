from django.urls import path
from . import views

urlpatterns = [
    # Página de búsqueda
    path('busqueda/', views.busqueda, name='busqueda'),

    # Lista de productos (también sirve como inicio)
    path('productos/', views.lista_productos, name='lista_productos'),
    path('', views.lista_productos, name='inicio'),

    # Vista de detalle de un producto
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),

    # Endpoints para el modal (JSON)
    path('<int:producto_id>/tallas/', views.obtener_tallas, name='obtener_tallas'),
    path('<int:producto_id>/colores/', views.obtener_colores, name='obtener_colores'),
]