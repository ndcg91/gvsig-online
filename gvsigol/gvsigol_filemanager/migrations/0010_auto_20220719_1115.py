# Generated by Django 2.2.18 on 2022-07-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_filemanager', '0009_auto_20220719_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exports_historical',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
