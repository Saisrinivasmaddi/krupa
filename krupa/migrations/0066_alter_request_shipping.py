# Generated by Django 5.1 on 2024-11-26 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0065_remove_shippingaddress_request_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='shipping',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='krupa.shippingaddress'),
        ),
    ]
