from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.carrito, name='carrito'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('', views.ver_carrito, name='ver_carrito'),
    path('', views.carrito, name='carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]