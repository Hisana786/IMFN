# Generated by Django 5.1.4 on 2025-03-19 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0009_transferpatient'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicines',
            name='Pharmacy_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imfnapp.pharmacy'),
        ),
    ]
