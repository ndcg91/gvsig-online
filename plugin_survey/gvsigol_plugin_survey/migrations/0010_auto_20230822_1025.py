# Generated by Django 2.2.28 on 2023-08-22 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_plugin_survey', '0009_auto_20210223_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyreadgroup',
            name='role',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='surveywritegroup',
            name='role',
            field=models.TextField(default=None),
        ),
    ]
