# Generated by Django 5.0.6 on 2024-06-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_remove_destinosturisticos_estadodestino'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinosturisticos',
            name='fechaTour',
            field=models.DateField(blank=True, null=True),
        ),
    ]
