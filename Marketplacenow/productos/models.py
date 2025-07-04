from django.db import models
from django.contrib.auth.models import User

# Categoría del producto
class Categoria(models.Model):
    ID_CATEGORIA = models.AutoField(primary_key=True)
    NOMBRE_CATEGORIA = models.CharField(max_length=30)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.NOMBRE_CATEGORIA


# Talla del producto
class Talla(models.Model):
    ID_TALLA = models.AutoField(primary_key=True)
    VALOR_TALLA = models.CharField(max_length=10)

    class Meta:
        db_table = 'talla'

    def __str__(self):
        return self.VALOR_TALLA


# Marca (✅ ahora puede ser ManyToMany si deseas múltiples marcas por producto)
class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'marca'

    def __str__(self):
        return self.nombre


# Color
class Color(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        db_table = 'color'

    def __str__(self):
        return self.nombre


# Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    tallas = models.ManyToManyField(Talla, blank=True)
    colores = models.ManyToManyField(Color, blank=True)
    marcas = models.ManyToManyField(Marca, blank=True)  # ✅ Convertido a ManyToMany

    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.nombre
    

class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    agregado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'producto')
        db_table = 'favorito'

    def __str__(self):
        return f"{self.usuario.username} ❤ {self.producto.nombre}"