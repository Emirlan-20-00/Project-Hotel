# Generated by Django 5.1.2 on 2024-10-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='address',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
