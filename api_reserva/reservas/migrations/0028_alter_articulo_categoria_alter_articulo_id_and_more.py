# Generated by Django 5.0.4 on 2024-05-13 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0027_articulo_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.categoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.proveedor'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(blank=True, choices=[], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='clientenet',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]