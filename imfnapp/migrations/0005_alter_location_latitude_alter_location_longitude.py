# Generated by Django 5.1.4 on 2025-03-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0004_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.CharField(max_length=9),
        ),
    ]
