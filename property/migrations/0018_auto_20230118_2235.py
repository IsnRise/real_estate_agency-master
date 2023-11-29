# Generated by Django 2.2.24 on 2023-01-18 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20230117_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]