# Generated by Django 2.2.18 on 2022-07-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_filemanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exports_historical',
            name='username',
            field=models.CharField(default='carlesmarti', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exports_historical',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]
