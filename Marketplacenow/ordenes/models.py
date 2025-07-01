from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto, Talla, Color

class Orden(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    class Meta:
        db_table = 'orden'

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"


class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name='detalles', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    talla = models.ForeignKey(Talla, null=True, blank=True, on_delete=models.SET_NULL)
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'detalle_orden'

    def subtotal(self):
        return self.cantidad * self.precio_unitario