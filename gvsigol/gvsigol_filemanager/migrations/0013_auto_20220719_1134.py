# Generated by Django 2.2.18 on 2022-07-19 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_filemanager', '0012_auto_20220719_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exports_historical',
            name='date',
        ),
        migrations.AlterField(
            model_name='exports_historical',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]
