# Generated by Django 5.0.4 on 2024-05-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0028_alter_articulo_categoria_alter_articulo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=100),
        ),
    ]
