# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-07-20 14:08


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_services', '0032_serviceurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='source_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
