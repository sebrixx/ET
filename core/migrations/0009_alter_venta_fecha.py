# Generated by Django 4.2.2 on 2023-06-22 00:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_detalle_detalleventa_alter_venta_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 0, 29, 12, 647033, tzinfo=datetime.timezone.utc)),
        ),
    ]
