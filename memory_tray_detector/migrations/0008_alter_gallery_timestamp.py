# Generated by Django 4.2.1 on 2023-05-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory_tray_detector', '0007_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
