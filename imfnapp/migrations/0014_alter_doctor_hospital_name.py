# Generated by Django 5.1.4 on 2025-02-17 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0013_alter_doctor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imfnapp.hospital'),
        ),
    ]
