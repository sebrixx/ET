# Generated by Django 4.2.2 on 2023-06-23 04:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_venta_fecha_delete_plantas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 4, 51, 16, 238324, tzinfo=datetime.timezone.utc)),
        ),
    ]
