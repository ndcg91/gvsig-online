# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-10-02 09:54


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_services', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='layergroup',
            name='toc_order',
            field=models.TextField(blank=True, null=True),
        ),
    ]
