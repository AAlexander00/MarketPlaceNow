from django.contrib import admin
from .models import Producto, Categoria, Talla

admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Talla)