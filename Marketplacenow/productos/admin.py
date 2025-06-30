from django.contrib import admin
from .models import Producto, Categoria, Talla, Color, Marca

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria', 'mostrar_marca', 'publicado_por')
    list_filter = ('categoria',)  # ✅ No se pueden usar ManyToManyField directamente aquí
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('tallas', 'colores')  # ✅ Para ManyToManyField en el admin

    # ✅ Agrupación de campos en el formulario
    fieldsets = (
        ('Información general', {
            'fields': ('nombre', 'descripcion', 'categoria', 'precio', 'stock')
        }),
        ('Variantes y Marca', {
            'fields': ('tallas', 'colores', 'marca')
        }),
        ('Multimedia y Publicación', {
            'fields': ('imagen', 'publicado_por')
        }),
    )

    def mostrar_marca(self, obj):
        return obj.marca.nombre if obj.marca else 'Sin marca'
    mostrar_marca.short_description = 'Marca'

# ✅ Registro del resto de modelos
admin.site.register(Categoria)
admin.site.register(Talla)
admin.site.register(Color)
admin.site.register(Marca)