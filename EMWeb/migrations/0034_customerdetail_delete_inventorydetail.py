# Generated by Django 4.0.4 on 2022-06-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0033_alter_btdetail_maxamp_alter_btdetail_maxvolt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ship_No', models.IntegerField(blank=True, null=True)),
                ('Cell_Type', models.CharField(blank=True, max_length=200, null=True)),
                ('Cell_qty', models.IntegerField(blank=True, null=True)),
                ('BMS_Type', models.CharField(blank=True, max_length=200, null=True)),
                ('BMSType', models.CharField(blank=True, max_length=200, null=True)),
                ('BMS_qty', models.IntegerField(blank=True, null=True)),
                ('Battery_pack', models.CharField(blank=True, max_length=200, null=True)),
                ('Battery_pack_qty', models.IntegerField(blank=True, null=True)),
                ('Bike_pack', models.CharField(blank=True, max_length=200, null=True)),
                ('Bike_pack_qty', models.IntegerField(blank=True, null=True)),
                ('motor_type', models.CharField(blank=True, max_length=200, null=True)),
                ('motor_qty', models.IntegerField(blank=True, null=True)),
                ('controller_type', models.CharField(blank=True, max_length=200, null=True)),
                ('controller_qty', models.IntegerField(blank=True, null=True)),
                ('throttle', models.IntegerField(blank=True, null=True)),
                ('brake', models.IntegerField(blank=True, null=True)),
                ('spokes', models.IntegerField(blank=True, null=True)),
                ('enclosure', models.IntegerField(blank=True, null=True)),
                ('breaker', models.IntegerField(blank=True, null=True)),
                ('display', models.IntegerField(blank=True, null=True)),
                ('B_Connector', models.IntegerField(blank=True, null=True)),
                ('wire', models.IntegerField(blank=True, null=True)),
                ('thimble', models.IntegerField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_number', models.CharField(blank=True, max_length=200, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=200, null=True)),
                ('delivery_type', models.CharField(blank=True, max_length=200, null=True)),
                ('Description', models.CharField(blank=True, max_length=200, null=True)),
                ('DatePur', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('User', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'customer_detail',
            },
        ),
        migrations.DeleteModel(
            name='Inventorydetail',
        ),
    ]
