# Generated by Django 2.2.24 on 2023-01-10 15:39

from django.db import migrations


def flat_to_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner, created = Owner.objects.get_or_create(
            name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
        )

        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20230110_1839'),
    ]

    operations = [
        migrations.RunPython(flat_to_owner),
    ]