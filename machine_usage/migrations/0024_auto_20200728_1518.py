# Generated by Django 2.2.14 on 2020-07-28 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machine_usage', '0023_userprofile_entertainment_mode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineslot',
            name='allowed_resources',
        ),
        migrations.RemoveField(
            model_name='machineslot',
            name='machine_type',
        ),
        migrations.RemoveField(
            model_name='slotusage',
            name='machine_slot',
        ),
        migrations.RemoveField(
            model_name='slotusage',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='slotusage',
            name='usage',
        ),
        migrations.RemoveField(
            model_name='usage',
            name='machine',
        ),
        migrations.RemoveField(
            model_name='usage',
            name='userprofile',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Machine',
        ),
        migrations.DeleteModel(
            name='MachineSlot',
        ),
        migrations.DeleteModel(
            name='MachineType',
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.DeleteModel(
            name='SlotUsage',
        ),
        migrations.DeleteModel(
            name='Usage',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
