# from django.db import models

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