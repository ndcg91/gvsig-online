# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-24 17:14


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_plugin_downloadman', '0003_auto_20190924_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downloadlog',
            old_name='laye_id_type',
            new_name='layer_id_type',
        ),
        migrations.RenameField(
            model_name='resourcelocator',
            old_name='laye_id_type',
            new_name='layer_id_type',
        ),
    ]
