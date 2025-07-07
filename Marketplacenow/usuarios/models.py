from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class Usuario(models.Model):
#     id_usuario = models.AutoField(db_column='ID_USUARIO', primary_key=True)
#     id_carrito = models.IntegerField(db_column='ID_CARRITO')
#     nombres_usuario = models.CharField(db_column='NOMBRES_USUARIO', max_length=30)
#     correoe = models.CharField(db_column='CORREOE', max_length=30)
#     contrasena = models.CharField(db_column='CONTRASENA', max_length=30)
#     direccion = models.CharField(db_column='DIRECCION', max_length=30, null=True)
#     telefono = models.IntegerField(db_column='TELEFONO', null=True)
#     fecharegistro = models.DateField(db_column='FECHAREGISTRO')
#     token = models.CharField(db_column='token', max_length=255)
#     token_expira = models.DateTimeField(db_column='token_expira')

#     class Meta:
#         db_table = 'usuario'


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    genero = models.CharField(
        max_length=20,
        choices=[
            ('Mujer', 'Mujer'),
            ('Hombre', 'Hombre'),
            ('Otro', 'Prefiero No Decir')
        ],
        null=True,  # <- permite valores nulos en la base de datos
        blank=True  # <- permite campos vacíos en formularios
    )

    fecha_nacimiento = models.DateField(
        null=True,  # <- permite valores nulos en la base de datos
        blank=True  # <- permite campos vacíos en formularios
    )

    def __str__(self):
        return f"Perfil de {self.user.username}"
    

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(user=instance)


from django.db import models
from django.contrib.auth.models import User

class Direccion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"Dirección de {self.usuario.username}"
