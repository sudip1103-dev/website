# Generated by Django 2.2.8 on 2020-01-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_usage', '0019_usage_failed'),
    ]

    operations = [
        migrations.AddField(
            model_name='usage',
            name='error',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usage',
            name='status_message',
            field=models.CharField(default='In Progress.', max_length=255),
        ),
    ]
