# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-10-20 14:47


from django.db import migrations
import ast, json

def set_default_images_as_empty(apps, schema_editor):
    #TODO
    try:
        from gvsigol_core.models import get_default_project_image, get_default_logo_image
        Project = apps.get_model("gvsigol_core", "Project")
        for project in Project.objects.all():
            if project.image and project.image.name == get_default_project_image():
                project.image = ''
            
            if project.logo and project.logo.name == get_default_logo_image():
                project.logo = ''
            project.save()
    except Exception as error:
        import logging
        logger = logging.getLogger()
        #logging.basicConfig()
        logger.exception(str(error))
        print(error)
        
class Migration(migrations.Migration):
    dependencies = [
        ('gvsigol_core', '0034_project_labels'),
    ]

    operations = [
        migrations.RunPython(set_default_images_as_empty, reverse_code=migrations.RunPython.noop),
    ]
