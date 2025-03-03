# Generated by Django 5.1.4 on 2025-02-26 22:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0030_alter_patient_login_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Cancel_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Login_id',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='imfnapp.login'),
        ),
    ]
