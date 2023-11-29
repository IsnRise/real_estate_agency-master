# Generated by Django 2.2.24 on 2022-12-18 15:34

from django.db import migrations


def copy_owners_from_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        Owner.objects.get_or_create(name=flat.owner, defaults={
            'owners_phonenumber': flat.owners_phonenumber,
        })

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(copy_owners_from_flats),
    ]
