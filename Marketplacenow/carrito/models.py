from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User

class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.producto.PRECIO * self.cantidad

    def __str__(self):
        return f"{self.producto.NOMBRE_PRODUCTO} x {self.cantidad}"
