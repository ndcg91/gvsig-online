# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-10-30 07:43


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_services', '0012_layergroup_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='workspace',
            name='wmts_endpoint',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
