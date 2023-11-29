# Generated by Django 2.2.24 on 2022-12-13 15:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owners_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Номер владельца'),
        ),
    ]
