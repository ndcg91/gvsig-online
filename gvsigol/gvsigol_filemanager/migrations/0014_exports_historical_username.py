# Generated by Django 2.2.18 on 2022-07-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_filemanager', '0013_auto_20220719_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='exports_historical',
            name='username',
            field=models.CharField(default='carlesmarti', max_length=30),
            preserve_default=False,
        ),
    ]
