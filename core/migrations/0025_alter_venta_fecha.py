# Generated by Django 4.2.2 on 2023-06-24 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_cactus_porcentaje_oferta_producto_porcentaje_oferta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 4, 58, 52, 27435, tzinfo=datetime.timezone.utc)),
        ),
    ]