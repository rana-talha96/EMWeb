# Generated by Django 4.0.4 on 2022-07-26 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0048_alter_celldetail_cell_pup'),
    ]

    operations = [
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='B_Connector_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='breaker_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='display_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='enclosure_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='thimble_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='batteryaccessorydetail',
            name='wire_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='batterypackdetail',
            name='Battery_pack_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='brake_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='controller_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='motor_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='spokes_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bikeaccessorydetail',
            name='throttle_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bikepackdetail',
            name='Bike_pack_PUP',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='bmsdetail',
            name='BMS_PUP',
            field=models.FloatField(default=0),
        ),
    ]
