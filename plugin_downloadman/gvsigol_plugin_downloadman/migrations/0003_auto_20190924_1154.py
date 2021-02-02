# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-24 11:54


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_plugin_downloadman', '0002_auto_20190921_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resourcelocator',
            name='ds_type',
        ),
        migrations.AlterField(
            model_name='downloadlog',
            name='laye_id_type',
            field=models.CharField(choices=[('GN', 'GEONET_DATA_SOURCE'), ('GV', 'GVSIGOL_DATA_SOURCE')], max_length=2),
        ),
        migrations.AlterField(
            model_name='resourcelocator',
            name='laye_id_type',
            field=models.CharField(choices=[('GN', 'GEONET_DATA_SOURCE'), ('GV', 'GVSIGOL_DATA_SOURCE')], max_length=2),
        ),
    ]
