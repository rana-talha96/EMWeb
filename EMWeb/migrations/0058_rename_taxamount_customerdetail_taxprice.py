# Generated by Django 4.0.4 on 2022-08-13 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0057_customerdetail_bms_price_customerdetail_bms_price1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetail',
            old_name='taxamount',
            new_name='taxprice',
        ),
    ]
