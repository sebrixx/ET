# Generated by Django 4.2.2 on 2023-06-23 20:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cactus',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='decorocion',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='maceteros',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='suculentas',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='sustratos',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='utensilios',
            name='oferta',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 20, 37, 2, 393164, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Plantas',
            fields=[
                ('codigo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80)),
                ('descripcion', models.CharField(max_length=450)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imagen', models.CharField(max_length=200)),
                ('oferta', models.BooleanField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
