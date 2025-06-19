from django.urls import path
from . import views
urlpatterns = [
    path('busqueda/', views.busqueda, name='busqueda'),
    path('productos/', views.lista_productos, name='lista_productos'),
]