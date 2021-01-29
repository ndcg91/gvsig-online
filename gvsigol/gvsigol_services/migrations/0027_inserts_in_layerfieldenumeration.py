# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2019-05-03 10:34

from django.db import migrations
import json

def inserts_in_layerfieldenumeration(apps, schema_editor):
    try:
        Layer = apps.get_model("gvsigol_services", "Layer")
        LayerFieldEnumeration = apps.get_model("gvsigol_services", "LayerFieldEnumeration")
        Enumeration = apps.get_model("gvsigol_services", "Enumeration")
        layers = Layer.objects.filter(type='v_PostGIS')
        for lyr in layers:
            ds_name = lyr.datastore.name
            sql = "SELECT * FROM information_schema.columns WHERE table_schema = '" + ds_name + "' AND table_name = '" + lyr.name + "'"
            cursor = schema_editor.connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            print("->Analizando capa %s.%s" % (ds_name, lyr.name))
            for i in rows:
                if(i[3].startswith("enm_") or i[3].startswith("enmm_")):
                    print("->Capa %s.%s columna %s es enumerada" % (ds_name, lyr.name, i[3]))
                    enum = None
                    try:
                        enum = Enumeration.objects.get(name = i[3])
                    except Exception:
                        print("->No se ha encontrado un enumerado para la capa %s.%s columna %s" % (ds_name, lyr.name, i[3]))
                        continue
                    if(enum is not None):
                        print("->Existe una enumeracion para la capa %s.%s columna %s" % (ds_name, lyr.name, i[3]))
                        lfe = LayerFieldEnumeration()
                        lfe.layername = lyr.name
                        lfe.schema = ds_name
                        lfe.field = i[3]
                        lfe.enumeration_id = enum.id 
                        if(i[3].startswith("enmm_")):
                            lfe.multiple = True
                        else:
                            lfe.multiple = False
                        lfe.save()
                        print("-> Migrado el campo enumerado %s a la version nueva" % i[3])
                    
    except Exception as error:
        print(error)
        

class Migration(migrations.Migration):

    dependencies = [
         ('gvsigol_services', '0026_remove_layerfieldenumeration_lyrid'),
    ]

    operations = [
        migrations.RunPython(inserts_in_layerfieldenumeration, reverse_code=migrations.RunPython.noop),
    ]