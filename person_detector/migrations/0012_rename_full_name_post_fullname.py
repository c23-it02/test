# Generated by Django 4.2.1 on 2023-05-18 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person_detector', '0011_post_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='full_name',
            new_name='fullName',
        ),
    ]
