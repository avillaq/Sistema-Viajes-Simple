# Generated by Django 5.0.6 on 2024-06-03 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Destination',
            new_name='DestinosTuristicos',
        ),
        migrations.RenameField(
            model_name='destinosturisticos',
            old_name='desc',
            new_name='descripcionCiudad',
        ),
        migrations.RenameField(
            model_name='destinosturisticos',
            old_name='img',
            new_name='imagenCiudad',
        ),
        migrations.RenameField(
            model_name='destinosturisticos',
            old_name='name',
            new_name='nombreCiudad',
        ),
        migrations.RenameField(
            model_name='destinosturisticos',
            old_name='offer',
            new_name='ofertaTour',
        ),
        migrations.RenameField(
            model_name='destinosturisticos',
            old_name='price',
            new_name='precioTour',
        ),
    ]
