# Generated by Django 4.2.2 on 2023-06-23 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 5, 10, 35, 193073, tzinfo=datetime.timezone.utc)),
        ),
    ]
