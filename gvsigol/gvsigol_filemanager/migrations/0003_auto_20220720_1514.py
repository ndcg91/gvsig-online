# Generated by Django 2.2.18 on 2022-07-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_filemanager', '0002_auto_20220720_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exports_historical',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
