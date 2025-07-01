from django.contrib import admin
from .models import Producto, Categoria, Talla, Color, Marca

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria', 'mostrar_marcas', 'publicado_por')
    list_filter = ('categoria',)  # ✅ No se pueden usar ManyToManyField directamente aquí
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('tallas', 'colores', 'marcas')  # ✅ Para ManyToManyField en el admin

    # ✅ Agrupación de campos en el formulario del admin
    fieldsets = (
        ('Información general', {
            'fields': ('nombre', 'descripcion', 'categoria', 'precio', 'stock')
        }),
        ('Variantes y Marcas', {
            'fields': ('tallas', 'colores', 'marcas')  # ← corregido a 'marcas'
        }),
        ('Multimedia y Publicación', {
            'fields': ('imagen', 'publicado_por')
        }),
    )

    def mostrar_marcas(self, obj):
        return ", ".join([marca.nombre for marca in obj.marcas.all()]) if obj.marcas.exists() else "Sin marca"
    mostrar_marcas.short_description = 'Marcas'

# ✅ Registro del resto de modelos
admin.site.register(Categoria)
admin.site.register(Talla)
admin.site.register(Color)
admin.site.register(Marca)