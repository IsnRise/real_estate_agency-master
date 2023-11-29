# Generated by Django 2.2.24 on 2022-12-02 16:24

from django.db import migrations


def is_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2016).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2016).update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(is_new_building)
    ]
