# Generated by Django 4.2.2 on 2023-06-22 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_decorocion_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 22, 0, 0, 59, 452787, tzinfo=datetime.timezone.utc)),
        ),
    ]
