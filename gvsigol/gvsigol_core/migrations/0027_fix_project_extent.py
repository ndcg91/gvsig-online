# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-06-19 08:09


from django.db import migrations

def fix_extent(apps, schema_editor):
    try:
        Project = apps.get_model("gvsigol_core", "Project")
        from gvsigol_core.utils import get_canonical_epsg3857_extent
        for p in Project.objects.all():
            p.extent = get_canonical_epsg3857_extent(p.extent)
            p.save()
            
    except Exception as error:
        print(str(error))

class Migration(migrations.Migration):

    dependencies = [
        ('gvsigol_core', '0026_projectbaselayertiling'),
    ]

    operations = [
        migrations.RunPython(fix_extent, reverse_code=migrations.RunPython.noop),
    ]
