from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_carrito, name='ver_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('pagar/', views.pagar_carrito, name='pagar_carrito'),  # ✅ Aquí
]
