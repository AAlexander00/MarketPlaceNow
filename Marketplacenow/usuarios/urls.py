from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path(
        'olvide_contrasena/',
        auth_views.PasswordResetView.as_view(template_name='usuarios/olvide_contrasena.html'),
        name='olvide_contrasena'
    ),
    path('perfil/', views.perfil, name='perfil'),
]