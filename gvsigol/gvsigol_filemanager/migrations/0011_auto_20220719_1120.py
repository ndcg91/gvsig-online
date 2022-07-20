# Generated by Django 2.2.18 on 2022-07-19 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_filemanager', '0010_auto_20220719_1115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exports_historical',
            name='time',
        ),
        migrations.AddField(
            model_name='exports_historical',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
