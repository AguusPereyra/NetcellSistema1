# Generated by Django 5.0.4 on 2024-05-10 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0026_articulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
