# Generated by Django 4.0.4 on 2022-06-22 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EMWeb', '0028_rename_description_celldetail_celldescription_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bmsdetail',
            old_name='Description',
            new_name='BMSDescription',
        ),
        migrations.RenameField(
            model_name='bmsdetail',
            old_name='InvoiceNo',
            new_name='BMSInvoiceNo',
        ),
    ]
