# Generated by Django 4.2.1 on 2023-05-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person_detector', '0003_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
