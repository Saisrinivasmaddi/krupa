# Generated by Django 5.1 on 2024-11-16 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0044_rename_due_date_invoiceestimate_expiry_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estimate',
            old_name='estimate_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='invoiceestimate',
            old_name='invoice_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='salesorder',
            old_name='sales_order_date',
            new_name='date',
        ),
    ]
