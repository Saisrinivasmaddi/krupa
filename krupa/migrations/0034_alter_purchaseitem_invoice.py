# Generated by Django 5.1 on 2024-11-04 03:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0033_purchase_purchaseitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitem',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='krupa.purchase'),
        ),
    ]
