from django.urls import path
from . import views

urlpatterns = [
    path('orden/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),
    path('orden/<int:orden_id>/pagar/', views.pagar_orden, name='pagar_orden'),
    path('ordenar/<int:producto_id>/', views.ordenar_producto, name='ordenar_producto'),
]