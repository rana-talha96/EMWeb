# Generated by Django 4.0.4 on 2022-06-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0018_alter_inventorydetail_bms_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorydetail',
            name='BMS_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='B_Connector',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='Battery_pack_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='Bike_pack_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='Cell_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='Description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='brake',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='breaker',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='controller_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='display',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='enclosure',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='motor_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='spokes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='thimble',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='throttle',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='inventorydetail',
            name='wire',
            field=models.IntegerField(null=True),
        ),
    ]
