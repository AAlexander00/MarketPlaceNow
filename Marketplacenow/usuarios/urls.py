from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('olvide_contrasena/', views.olvide_contrasena, name='olvide_contrasena'),
    path('perfil/', views.perfil, name='perfil'),
]