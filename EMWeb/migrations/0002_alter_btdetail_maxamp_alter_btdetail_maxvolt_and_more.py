# Generated by Django 4.1.dev20220407055456 on 2022-04-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btdetail',
            name='MaxAmp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btdetail',
            name='MaxVolt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btdetail',
            name='MinAmp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btdetail',
            name='MinVolt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btdetail',
            name='SCMaxVolt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btdetail',
            name='SCMinVolt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='btdetail',
            name='Temp',
            field=models.IntegerField(),
        ),
    ]