# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-09-12 10:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_plugin_catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='layermetadata',
            name='metadata_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
