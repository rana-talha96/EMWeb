# Generated by Django 4.0.4 on 2022-08-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0060_alter_customerdetail_bms_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetail',
            name='BMS_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='BMS_price1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='BMS_price2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='B_Connector_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Battery_pack_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Bike_pack_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Cell_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Cell_price1',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Cell_price2',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Cell_price3',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='Cell_price4',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='brake_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='breaker_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='controller_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='display_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='enclosure_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='motor_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='spokes_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='thimble_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='throttle_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customerdetail',
            name='wire_price',
            field=models.FloatField(default=0),
        ),
    ]
