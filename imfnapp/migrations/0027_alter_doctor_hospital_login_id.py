# Generated by Django 5.1.4 on 2025-02-21 11:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0026_alter_doctor_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital_login_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_login', to='imfnapp.login'),
        ),
    ]
