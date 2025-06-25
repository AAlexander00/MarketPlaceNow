from django.urls import path
from . import views

urlpatterns = [
    path('pagar/<int:orden_id>/', views.pagar_orden, name='pagar_orden'),
    path('confirmacion/', views.confirmacion_pago, name='confirmacion_pago'),
]