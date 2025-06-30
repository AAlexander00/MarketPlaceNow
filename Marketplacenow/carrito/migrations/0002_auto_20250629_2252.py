from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),  # reemplaza por la anterior
        ('productos', '0001_initial'),  # asegúrate que productos esté listado si usas ForeignKey a Talla/Color
    ]

    operations = [
        migrations.AddField(
            model_name='carritoitem',
            name='talla',
            field=models.ForeignKey(null=True, blank=True, to='productos.talla', on_delete=django.db.models.deletion.SET_NULL),
        ),
        migrations.AddField(
            model_name='carritoitem',
            name='color',
            field=models.ForeignKey(null=True, blank=True, to='productos.color', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]