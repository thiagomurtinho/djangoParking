# Generated by Django 2.2.3 on 2019-07-27 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rotarymonthly'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rotarymonthly',
            old_name='totaPaid',
            new_name='totalPaid',
        ),
    ]
