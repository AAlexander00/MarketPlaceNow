from django.contrib import admin
from .models import Producto, Categoria, Talla, Color, Marca

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria', 'marca', 'publicado_por')
    list_filter = ('categoria', 'marca', 'tallas', 'colores')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('tallas', 'colores')

admin.site.register(Categoria)
admin.site.register(Talla)
admin.site.register(Color)
admin.site.register(Marca)