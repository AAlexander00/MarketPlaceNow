from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),  # ← Asegúrate de que sea la última migración válida
    ]

    operations = [
        migrations.CreateModel(
            name='producto_colores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('producto', models.ForeignKey(to='productos.producto', on_delete=models.CASCADE)),
                ('color', models.ForeignKey(to='productos.color', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'producto_colores',
                'managed': True,
            },
        ),
    ]