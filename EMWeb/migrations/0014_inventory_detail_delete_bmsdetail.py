# Generated by Django 4.0.4 on 2022-06-18 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0013_bmsdetail_user_alter_bmsdetail_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_detail',
            fields=[
                ('InvoiceNo', models.IntegerField(primary_key=True, serialize=False)),
                ('BMS_Type', models.CharField(default=1, max_length=200)),
                ('BMSType', models.CharField(max_length=200)),
                ('BMS_qty', models.IntegerField()),
                ('Cell_Type', models.CharField(max_length=200)),
                ('Cell_qty', models.IntegerField()),
                ('Battery_pack', models.CharField(max_length=200)),
                ('Battery_pack_qty', models.IntegerField()),
                ('motor_type', models.CharField(max_length=200)),
                ('motor_qty', models.IntegerField()),
                ('controller_type', models.CharField(max_length=200)),
                ('controller_qty', models.IntegerField()),
                ('throttle', models.IntegerField()),
                ('brake', models.IntegerField()),
                ('spokes', models.IntegerField()),
                ('enclosure', models.IntegerField()),
                ('breaker', models.IntegerField()),
                ('display', models.IntegerField()),
                ('B_Connector', models.IntegerField()),
                ('wire', models.IntegerField()),
                ('thimble', models.IntegerField()),
                ('Description', models.CharField(max_length=200)),
                ('DatePur', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('User', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'inventory_detail',
            },
        ),
        migrations.DeleteModel(
            name='BMSdetail',
        ),
    ]
