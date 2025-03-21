# Generated by Django 5.1.4 on 2025-03-03 15:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Password', models.CharField(max_length=10)),
                ('user_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField(default=0)),
                ('Current_Date', models.DateField(auto_now_add=True)),
                ('Card_owner', models.CharField(max_length=25)),
                ('Card_no', models.CharField(max_length=16)),
                ('Exp_month', models.IntegerField()),
                ('Exp_year', models.IntegerField()),
                ('CVV', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospital_Name', models.CharField(max_length=25)),
                ('Address', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=30)),
                ('City', models.CharField(max_length=40)),
                ('Contact_No', models.CharField(max_length=15)),
                ('Login_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='imfnapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=25)),
                ('photo', models.FileField(upload_to='uploads')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=20)),
                ('DOB', models.DateField()),
                ('specialisation', models.CharField(max_length=40)),
                ('year_of_experience', models.CharField(max_length=20)),
                ('contact_no', models.CharField(max_length=15)),
                ('consultation_fee', models.IntegerField(default=0)),
                ('hospital_login_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_login', to='imfnapp.login')),
                ('login_id', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor_login', to='imfnapp.login')),
            ],
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(max_length=25)),
                ('Time', models.TimeField(max_length=25)),
                ('Current_Date', models.DateField(auto_now_add=True)),
                ('Payment_Status', models.IntegerField(default=0)),
                ('Cancel_status', models.IntegerField(default=0)),
                ('Url', models.URLField(blank=True, null=True)),
                ('doctor_login_id', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='imfnapp.login')),
                ('patient_login_id', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_login', to='imfnapp.login')),
            ],
        ),
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
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=25)),
                ('DOB', models.DateField()),
                ('contact_no', models.CharField(max_length=25)),
                ('Login_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='imfnapp.login')),
            ],
        ),
    ]
