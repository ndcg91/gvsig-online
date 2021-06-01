from django.urls import path
from gvsigol_services import views as services_views

urlpatterns = [
    path('server_list/', services_views.server_list, name='server_list'),
    path('server_add/', services_views.server_add, name='server_add'),
    path('server_delete/<int:svid>/', services_views.server_delete, name='server_delete'),
    path('server_update/<int:svid>/', services_views.server_update, name='server_update'), 
    path('get_server/<int:svid>/', services_views.get_server, name='get_server'),  
    path('reload_node/<int:nid>/', services_views.reload_node, name='reload_node'),
    path('workspace_list/', services_views.workspace_list, name='workspace_list'),
    path('workspace_add/', services_views.workspace_add, name='workspace_add'),
    path('workspace_import/', services_views.workspace_import, name='workspace_import'),
    path('workspace_delete/<int:wsid>/', services_views.workspace_delete, name='workspace_delete'),
    path('workspace_update/<int:wid>/', services_views.workspace_update, name='workspace_update'),
    path('datastore_list/', services_views.datastore_list, name='datastore_list'),
    path('datastore_add/', services_views.datastore_add, name='datastore_add'),
    path('datastore_update/<int:datastore_id>/', services_views.datastore_update, name='datastore_update'),
    path('datastore_delete/<int:dsid>/', services_views.datastore_delete, name='datastore_delete'),
    path('backend_datastore_list/', services_views.backend_datastore_list, name='backend_datastore_list'),
    path('backend_resource_list_available/', services_views.backend_resource_list_available, name='backend_resource_list_available'),
    path('backend_resource_list_configurable/', services_views.backend_resource_list_configurable, name='backend_resource_list_configurable'),
    path('backend_resource_list/', services_views.backend_resource_list, name='backend_resource_list'),
    path('backend_fields_list/', services_views.backend_fields_list, name='backend_fields_list'),
    path('backend_layergroup_list_available/', services_views.backend_layergroup_list_available, name='backend_layergroup_list_available'),
    path('layer_list/', services_views.layer_list, name='layer_list'),
    path('layer_add/', services_views.layer_add, name='layer_add'),
    path('layer_add/<int:layergroup_id>/', services_views.layer_add_with_group, name='layer_add_with_group'),
    path('get_resources_from_workspace/', services_views.get_resources_from_workspace, name='get_resources_from_workspace'),
    path('layer_update/<int:layer_id>/', services_views.layer_update, name='layer_update'),
    path('layer_delete/<int:layer_id>/', services_views.layer_delete, name='layer_delete'),
    path('layer_config/<int:layer_id>/', services_views.layer_config, name='layer_config'),
    path('convert_to_enumerate/', services_views.convert_to_enumerate, name='convert_to_enumerate'),
    path('layer_refresh_conf/<int:layer_id>/', services_views.layer_refresh_conf, name='layer_refresh_conf'),
    path('layer_cache_clear/<int:layer_id>/', services_views.layer_cache_clear, name='layer_cache_clear'),
    path('layergroup_cache_clear/<int:layergroup_id>/', services_views.layergroup_cache_clear, name='layergroup_cache_clear'),
    path('layer_create/', services_views.layer_create, name='layer_create'),
    path('layer_create/<int:layergroup_id>/', services_views.layer_create_with_group, name='layer_create_with_group'),
    path('get_geom_tables/<int:datastore_id>/', services_views.get_geom_tables, name='geom_tables'),
    path('layergroup_list/', services_views.layergroup_list, name='layergroup_list'),
    path('layergroup_add/', services_views.layergroup_add, name='layergroup_add'),
    path('layergroup_add/<int:project_id>/', services_views.layergroup_add_with_project, name='layergroup_add_with_project'),
    path('layergroup_delete/<int:lgid>/', services_views.layergroup_delete, name='layergroup_delete'),
    path('layergroup_update/<int:lgid>/', services_views.layergroup_update, name='layergroup_update'),
    path('enumeration_list/', services_views.enumeration_list, name='enumeration_list'),
    path('enumeration_add/', services_views.enumeration_add, name='enumeration_add'),
    path('enumeration_delete/<int:eid>/', services_views.enumeration_delete, name='enumeration_delete'),
    path('enumeration_update/<int:eid>/', services_views.enumeration_update, name='enumeration_update'),
    path('get_enumeration/', services_views.get_enumeration, name='get_enumeration'),
    path('layer_boundingbox_from_data/', services_views.layer_boundingbox_from_data, name='layer_boundingbox_from_data'),
    path('add_layer_lock/', services_views.add_layer_lock, name='add_layer_lock'),
    path('remove_layer_lock/', services_views.remove_layer_lock, name='remove_layer_lock'),
    path('lock_list/', services_views.lock_list, name='lock_list'),
    path('unlock_layer/<int:lock_id>/', services_views.unlock_layer, name='unlock_layer'),
    path('get_feature_info/', services_views.get_feature_info, name='get_feature_info'),
    path('get_datatable_data/', services_views.get_datatable_data, name='get_datatable_data'),
    path('get_feature_wfs/', services_views.get_feature_wfs, name='get_feature_wfs'),
    path('get_unique_values/', services_views.get_unique_values, name='get_unique_values'),
    path('get_feature_resources/', services_views.get_feature_resources, name='get_feature_resources'),
    path('get_resource/<int:resource_id>/', services_views.get_resource, name='get_layer_resource'),
    path('upload_resources/', services_views.upload_resources, name='upload_resources'),
    path('delete_resource/', services_views.delete_resource, name='delete_resource'),
    path('delete_resources/', services_views.delete_resources, name='delete_resources'),
    path('describeFeatureType/', services_views.describeFeatureType, name='describeFeatureType'),
    path('describeFeatureTypeWithPk/', services_views.describeFeatureTypeWithPk, name='describeFeatureTypeWithPk'),
    path('external_layer_list/', services_views.external_layer_list, name='external_layer_list'),
    path('external_layer_add/', services_views.external_layer_add, name='external_layer_add'),
    path('external_layer_update/<int:external_layer_id>/', services_views.external_layer_update, name='external_layer_update'),
    path('external_layer_delete/<int:external_layer_id>/', services_views.external_layer_delete, name='external_layer_delete'),
    path('get_capabilities_from_url/', services_views.get_capabilities_from_url, name='external_layer_get_capabilities'),
    path('get_capabilities/', services_views.get_capabilities, name='get_capabilities'),
    path('cache_list/', services_views.cache_list, name='cache_list'),
    path('layer_cache_config/<int:layer_id>/', services_views.layer_cache_config, name='layer_cache_config'),
    path('group_cache_config/<int:group_id>/', services_views.group_cache_config, name='group_cache_config'),
    path('get_cache_tasks/', services_views.get_cache_tasks, name='get_cache_tasks'),
    path('get_group_cache_tasks/', services_views.get_group_cache_tasks, name='get_group_cache_tasks'),
    path('kill_all_tasks/', services_views.kill_all_tasks, name='kill_all_tasks'),
    path('kill_all_group_tasks/', services_views.kill_all_group_tasks, name='kill_all_group_tasks'),
    path('create_base_layer/<int:pid>/', services_views.create_base_layer, name='create_base_layer'),
    path('base_layer_process_update/<int:pid>/', services_views.base_layer_process_update, name='base_layer_process_update'),
    path('stop_base_layer_process/<int:pid>/', services_views.stop_base_layer_process, name='stop_base_layer_process'),
    path('retry_base_layer_process/<int:pid>/', services_views.retry_base_layer_process, name='retry_base_layer_process'),
    path('layers_get_temporal_properties/', services_views.layers_get_temporal_properties, name='layers_get_temporal_properties'),
    path('get_date_fields_from_resource/', services_views.get_date_fields_from_resource, name='get_date_fields_from_resource'),
    path('describeLayerConfig/', services_views.describeLayerConfig, name='describeLayerConfig'),
    path('update_thumbnail/<int:layer_id>/', services_views.update_thumbnail, name='update_thumbnail'),
    path('nullable_check/', services_views.check_nullable, name='check_nullable'),
    path('service_url_list/', services_views.service_url_list, name='service_url_list'),
    path('service_url_add/', services_views.service_url_add, name='service_url_add'),
    path('service_url_delete/<int:svid>/', services_views.service_url_delete, name='service_url_delete'),
    path('service_url_update/<int:svid>/', services_views.service_url_update, name='service_url_update'),
    path('test_connection/', services_views.test_connection, name='test_connection'),
    path('register_action/', services_views.register_action, name='register_action'),
    path('db_field_delete/', services_views.db_field_delete, name='db_field_delete'),
    #path('db_field_changetype/', services_views.db_field_changetype, name='db_field_changetype'),
    path('db_field_rename/', services_views.db_field_rename, name='db_field_rename'),
    path('db_field_add/', services_views.db_add_field, name='db_field_add'),
]
