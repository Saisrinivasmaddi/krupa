# Generated by Django 5.1 on 2024-10-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krupa', '0024_estimate_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='status',
            field=models.CharField(blank=True, default='SENT', max_length=30, null=True),
        ),
    ]
