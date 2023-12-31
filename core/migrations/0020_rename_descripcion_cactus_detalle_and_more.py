# Generated by Django 4.2.2 on 2023-06-23 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_venta_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cactus',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='decorocion',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='maceteros',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='plantas',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='suculentas',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='sustratos',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.RenameField(
            model_name='utensilios',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 21, 13, 45, 628124, tzinfo=datetime.timezone.utc)),
        ),
    ]
