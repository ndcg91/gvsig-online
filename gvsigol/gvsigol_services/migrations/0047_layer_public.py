# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2021-02-15 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_services', '0046_fix_uppercase_field_triggers'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
