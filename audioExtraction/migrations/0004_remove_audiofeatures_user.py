# Generated by Django 4.2.4 on 2023-08-26 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioExtraction', '0003_audiofeatures_user_alter_audiofeatures_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofeatures',
            name='user',
        ),
    ]
