# Generated by Django 4.0.4 on 2022-08-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0056_customerdetail_taxamount_customerdetail_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdetail',
            name='BMS_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='BMS_price1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='BMS_price2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='B_Connector_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Battery_pack_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Bike_pack_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Cell_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Cell_price1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Cell_price2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Cell_price3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='Cell_price4',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='brake_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='breaker_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='controller_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='display_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='enclosure_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='motor_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='spokes_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='thimble_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='throttle_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customerdetail',
            name='wire_price',
            field=models.FloatField(default=0),
        ),
    ]