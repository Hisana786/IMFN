# Generated by Django 5.1.4 on 2025-01-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imfnapp', '0003_ambulance'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='user_type',
            field=models.CharField(default='hospital', max_length=10),
            preserve_default=False,
        ),
    ]
