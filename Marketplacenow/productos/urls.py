from django.urls import path
from . import views

urlpatterns = [
    path('busqueda/', views.busqueda, name='busqueda'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('', views.lista_productos, name='inicio'),
    path('<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('detalle/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]