# Generated by Django 4.2.2 on 2023-06-15 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_descripcion_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 15, 15, 53, 55, 17058, tzinfo=datetime.timezone.utc)),
        ),
    ]
