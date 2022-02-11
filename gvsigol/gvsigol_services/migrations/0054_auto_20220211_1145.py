# Generated by Django 2.2.21 on 2022-02-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_services', '0053_sqlview'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlview',
            name='created_by',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddConstraint(
            model_name='sqlview',
            constraint=models.UniqueConstraint(fields=('datastore', 'name'), name='unique_name_per_datastore'),
        ),
    ]
