# Generated by Django 4.0.4 on 2022-06-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0024_bikeaccessorydetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatteryAccessorydetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvoiceNo', models.IntegerField(null=True)),
                ('enclosure', models.IntegerField(null=True)),
                ('breaker', models.IntegerField(null=True)),
                ('display', models.IntegerField(null=True)),
                ('B_Connector', models.IntegerField(null=True)),
                ('wire', models.IntegerField(null=True)),
                ('thimble', models.IntegerField(null=True)),
                ('Description', models.CharField(max_length=200, null=True)),
                ('DatePur', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('User', models.CharField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'battery_accessory_detail',
            },
        ),
    ]
