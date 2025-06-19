from django.db import models

class Producto(models.Model):
    ID_PRODUCTO = models.AutoField(primary_key=True)
    ID_CATEGORIA = models.IntegerField()
    NOMBRE_PRODUCTO = models.CharField(max_length=100)
    DESCRIPCION = models.TextField()
    PRECIO = models.DecimalField(max_digits=10, decimal_places=2)
    FECHA_PUBLICACION = models.DateField()
    DIAS_GARANTIA = models.IntegerField()
    IMAGEN = models.CharField(max_length=150)

    class Meta:
        db_table = 'producto'