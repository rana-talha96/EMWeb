# Generated by Django 4.0.4 on 2022-08-14 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0058_rename_taxamount_customerdetail_taxprice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetail',
            old_name='subtotal',
            new_name='price',
        ),
    ]
