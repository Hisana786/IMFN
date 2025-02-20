# Generated by Django 5.1.4 on 2025-02-17 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0014_alter_doctor_hospital_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Login_id',
        ),
        migrations.AddField(
            model_name='doctor',
            name='login_id',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imfnapp.login'),
        ),
    ]
