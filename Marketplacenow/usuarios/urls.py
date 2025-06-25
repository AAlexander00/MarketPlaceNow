from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),

    # Recuperación de contraseña
    path('olvide_contrasena/', auth_views.PasswordResetView.as_view(
        template_name='usuarios/olvide_contrasena.html'), name='password_reset'),
    path('recuperar/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='usuarios/password_reset_done.html'), name='password_reset_done'),
    path('recuperar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='usuarios/password_reset_confirm.html'), name='password_reset_confirm'),
    path('recuperar/completo/', auth_views.PasswordResetCompleteView.as_view(
        template_name='usuarios/password_reset_complete.html'), name='password_reset_complete'),
]

from django.contrib.auth.views import LogoutView

urlpatterns += [
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
]