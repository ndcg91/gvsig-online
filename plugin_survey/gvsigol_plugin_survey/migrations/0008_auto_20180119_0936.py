# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-01-19 09:36


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_auth', '0001_initial'),
        ('gvsigol_plugin_survey', '0007_auto_20180115_0937'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyWriteGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gvsigol_plugin_survey.Survey')),
                ('user_group', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gvsigol_auth.UserGroup')),
            ],
        ),
        migrations.RenameModel(
            old_name='SurveyUserGroup',
            new_name='SurveyReadGroup',
        ),
    ]
