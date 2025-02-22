# Generated by Django 5.1.4 on 2025-01-06 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0002_hospital_login_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ambulance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ambulance_Category', models.CharField(max_length=35)),
                ('Ambulance_Type', models.CharField(max_length=50)),
                ('Vehicle_NO', models.CharField(max_length=15)),
                ('Contact_No', models.CharField(max_length=15)),
                ('Driver_Name', models.CharField(max_length=30)),
                ('Login_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imfnapp.login')),
            ],
        ),
    ]
