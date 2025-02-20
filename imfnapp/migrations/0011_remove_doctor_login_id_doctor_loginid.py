# Generated by Django 5.1.4 on 2025-02-16 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0010_remove_doctor_loginid_doctor_login_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='Login_id',
        ),
        migrations.AddField(
            model_name='doctor',
            name='loginid',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imfnapp.login'),
        ),
    ]
