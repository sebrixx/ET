# Generated by Django 4.1.5 on 2023-06-28 21:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0027_alter_venta_fecha"),
    ]

    operations = [
        migrations.AlterField(
            model_name="venta",
            name="fecha",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 28, 21, 22, 43, 740323, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
