# Generated by Django 4.0.4 on 2022-07-22 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0044_alter_customerdetail_bms_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='B_Connector_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='breaker_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='display_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='enclosure_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='thimble_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='wire_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='batterypackdetail',
            name='Battery_pack_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='brake_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='controller_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='motor_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='spokes_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='throttle_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bikepackdetail',
            name='Bike_pack_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='bmsdetail',
            name='BMS_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='celldetail',
            name='Cell_price',
            field=models.FloatField(null=True),
        ),
    ]
