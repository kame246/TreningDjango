# Generated by Django 4.2 on 2023-05-13 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'permissions': [('set_published_status', 'Can set the status of the post to either publish or not')]},
        ),
    ]
