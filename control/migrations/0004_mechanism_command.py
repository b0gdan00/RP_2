# Generated by Django 5.1.6 on 2025-04-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0003_sensor_command'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanism',
            name='command',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
