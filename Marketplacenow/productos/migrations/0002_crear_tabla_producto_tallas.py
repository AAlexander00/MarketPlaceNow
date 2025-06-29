from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),  # ✅ Asegúrate que coincide con tu última migración
    ]

    operations = [
        migrations.CreateModel(
            name='producto_tallas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.ForeignKey(to='productos.producto', on_delete=models.CASCADE)),
                ('talla', models.ForeignKey(to='productos.talla', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'producto_tallas',
                'managed': True,  # Esto le dice a Django que debe crear esta tabla
            },
        ),
    ]