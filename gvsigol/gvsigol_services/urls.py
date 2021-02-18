from django.conf.urls import url
from gvsigol_services import views as services_views

urlpatterns = [
    url(r'^server_list/$', services_views.server_list, name='server_list'),
    url(r'^server_add/$', services_views.server_add, name='server_add'),
    url(r'^server_delete/(?P<svid>\d+)/$', services_views.server_delete, name='server_delete'),
    url(r'^server_update/(?P<svid>[0-9]+)/$', services_views.server_update, name='server_update'), 
    url(r'^get_server/(?P<svid>\d+)/$', services_views.get_server, name='get_server'),  
    url(r'^reload_node/(?P<nid>\d+)/$', services_views.reload_node, name='reload_node'),
    url(r'^workspace_list/$', services_views.workspace_list, name='workspace_list'),
    url(r'^workspace_add/$', services_views.workspace_add, name='workspace_add'),
    url(r'^workspace_import/$', services_views.workspace_import, name='workspace_import'),
    url(r'^workspace_delete/(?P<wsid>\d+)/$', services_views.workspace_delete, name='workspace_delete'),
    url(r'^workspace_update/(?P<wid>[0-9]+)/$', services_views.workspace_update, name='workspace_update'),
    url(r'^datastore_list/$', services_views.datastore_list, name='datastore_list'),
    url(r'^datastore_add/$', services_views.datastore_add, name='datastore_add'),
    url(r'^datastore_update/(?P<datastore_id>[0-9]+)/$', services_views.datastore_update, name='datastore_update'),
    url(r'^datastore_delete/(?P<dsid>\d+)/$', services_views.datastore_delete, name='datastore_delete'),
    url(r'^backend_datastore_list/$', services_views.backend_datastore_list, name='backend_datastore_list'),
    url(r'^backend_resource_list_available/$', services_views.backend_resource_list_available, name='backend_resource_list_available'),
    url(r'^backend_resource_list_configurable/$', services_views.backend_resource_list_configurable, name='backend_resource_list_configurable'),
    url(r'^backend_resource_list/$', services_views.backend_resource_list, name='backend_resource_list'),
    url(r'^backend_fields_list/$', services_views.backend_fields_list, name='backend_fields_list'),
    url(r'^backend_layergroup_list_available/$', services_views.backend_layergroup_list_available, name='backend_layergroup_list_available'),
    url(r'^layer_list/$', services_views.layer_list, name='layer_list'),
    url(r'^layer_add/$', services_views.layer_add, name='layer_add'),
    url(r'^layer_add/(?P<layergroup_id>[0-9]+)/$', services_views.layer_add_with_group, name='layer_add_with_group'),
    url(r'^get_resources_from_workspace/$', services_views.get_resources_from_workspace, name='get_resources_from_workspace'),
    url(r'^layer_update/(?P<layer_id>[0-9]+)/$', services_views.layer_update, name='layer_update'),
    url(r'^layer_delete/(?P<layer_id>[0-9]+)/$', services_views.layer_delete, name='layer_delete'),
    url(r'^layer_config/(?P<layer_id>[0-9]+)/$', services_views.layer_config, name='layer_config'),
    url(r'^convert_to_enumerate/$', services_views.convert_to_enumerate, name='convert_to_enumerate'),
    url(r'^layer_cache_clear/(?P<layer_id>[0-9]+)/$', services_views.cache_clear, name='cache_clear'),
    url(r'^layer_refresh_extent/(?P<layer_id>[0-9]+)/$', services_views.layer_refresh_extent, name='layer_refresh_extent'),
    url(r'^manage_cache_clear/(?P<layer_id>[0-9]+)/$', services_views.manage_cache_clear, name='manage_cache_clear'),
    url(r'^group_cache_clear/(?P<layer_id>[0-9]+)/$', services_views.group_cache_clear, name='group_cache_clear'),
    url(r'^layergroup_cache_clear/(?P<layergroup_id>[0-9]+)/$', services_views.layergroup_cache_clear, name='layergroup_cache_clear'),
    url(r'^layer_create/$', services_views.layer_create, name='layer_create'),
    url(r'^layer_create/(?P<layergroup_id>[0-9]+)/$', services_views.layer_create_with_group, name='layer_create_with_group'),
    url(r'^get_geom_tables/(?P<datastore_id>[0-9]+)/$', services_views.get_geom_tables, name='geom_tables'),
    url(r'^layergroup_list/$', services_views.layergroup_list, name='layergroup_list'),
    url(r'^layergroup_add/$', services_views.layergroup_add, name='layergroup_add'),
    url(r'^layergroup_add/(?P<project_id>[0-9]+)/$', services_views.layergroup_add_with_project, name='layergroup_add_with_project'),
    url(r'^layergroup_delete/(?P<lgid>[0-9]+)/$', services_views.layergroup_delete, name='layergroup_delete'),
    url(r'^layergroup_update/(?P<lgid>[0-9]+)/$', services_views.layergroup_update, name='layergroup_update'),
    url(r'^enumeration_list/$', services_views.enumeration_list, name='enumeration_list'),
    url(r'^enumeration_add/$', services_views.enumeration_add, name='enumeration_add'),
    url(r'^enumeration_delete/(?P<eid>[0-9]+)/$', services_views.enumeration_delete, name='enumeration_delete'),
    url(r'^enumeration_update/(?P<eid>[0-9]+)/$', services_views.enumeration_update, name='enumeration_update'),
    url(r'^get_enumeration/$', services_views.get_enumeration, name='get_enumeration'),
    url(r'^layer_boundingbox_from_data/$', services_views.layer_boundingbox_from_data, name='layer_boundingbox_from_data'),
    url(r'^add_layer_lock/$', services_views.add_layer_lock, name='add_layer_lock'),
    url(r'^remove_layer_lock/$', services_views.remove_layer_lock, name='remove_layer_lock'),
    url(r'^lock_list/$', services_views.lock_list, name='lock_list'),
    url(r'^unlock_layer/(?P<lock_id>[0-9]+)/$', services_views.unlock_layer, name='unlock_layer'),
    url(r'^get_feature_info/$', services_views.get_feature_info, name='get_feature_info'),
    url(r'^get_datatable_data/$', services_views.get_datatable_data, name='get_datatable_data'),
    url(r'^get_feature_wfs/$', services_views.get_feature_wfs, name='get_feature_wfs'),
    url(r'^get_unique_values/$', services_views.get_unique_values, name='get_unique_values'),
    url(r'^get_feature_resources/$', services_views.get_feature_resources, name='get_feature_resources'),
    url(r'^get_resource/(?P<resource_id>[0-9]+)/$', services_views.get_resource, name='get_layer_resource'),
    url(r'^upload_resources/$', services_views.upload_resources, name='upload_resources'),
    url(r'^delete_resource/$', services_views.delete_resource, name='delete_resource'),
    url(r'^delete_resources/$', services_views.delete_resources, name='delete_resources'),
    url(r'^describeFeatureType/$', services_views.describeFeatureType, name='describeFeatureType'),
    url(r'^describeFeatureTypeWithPk/$', services_views.describeFeatureTypeWithPk, name='describeFeatureTypeWithPk'),
    url(r'^external_layer_list/$', services_views.external_layer_list, name='external_layer_list'),
    url(r'^external_layer_add/$', services_views.external_layer_add, name='external_layer_add'),
    url(r'^external_layer_update/(?P<external_layer_id>[0-9]+)/$', services_views.external_layer_update, name='external_layer_update'),
    url(r'^external_layer_delete/(?P<external_layer_id>[0-9]+)/$', services_views.external_layer_delete, name='external_layer_delete'),
    url(r'^get_capabilities_from_url/$', services_views.get_capabilities_from_url, name='external_layer_get_capabilities'),
    url(r'^get_capabilities/$', services_views.get_capabilities, name='get_capabilities'),
    url(r'^cache_list/$', services_views.cache_list, name='cache_list'),
    url(r'^layer_cache_config/(?P<layer_id>[0-9]+)/$', services_views.layer_cache_config, name='layer_cache_config'),
    url(r'^group_cache_config/(?P<group_id>[0-9]+)/$', services_views.group_cache_config, name='group_cache_config'),
    url(r'^get_cache_tasks/$', services_views.get_cache_tasks, name='get_cache_tasks'),
    url(r'^get_group_cache_tasks/$', services_views.get_group_cache_tasks, name='get_group_cache_tasks'),
    url(r'^kill_all_tasks/$', services_views.kill_all_tasks, name='kill_all_tasks'),
    url(r'^kill_all_group_tasks/$', services_views.kill_all_group_tasks, name='kill_all_group_tasks'),
    url(r'^create_base_layer/(?P<pid>[0-9]+)/$', services_views.create_base_layer, name='create_base_layer'),
    url(r'^base_layer_process_update/(?P<pid>[0-9]+)/$', services_views.base_layer_process_update, name='base_layer_process_update'),
    url(r'^stop_base_layer_process/(?P<pid>[0-9]+)/$', services_views.stop_base_layer_process, name='stop_base_layer_process'),
    url(r'^retry_base_layer_process/(?P<pid>[0-9]+)/$', services_views.retry_base_layer_process, name='retry_base_layer_process'),
    
    url(r'^layers_get_temporal_properties/$', services_views.layers_get_temporal_properties, name='layers_get_temporal_properties'),
    url(r'^get_date_fields_from_resource/$', services_views.get_date_fields_from_resource, name='get_date_fields_from_resource'),
        
    url(r'^describeLayerConfig/$', services_views.describeLayerConfig, name='describeLayerConfig'),
    
    url(r'^update_thumbnail/(?P<layer_id>[0-9]+)/$', services_views.update_thumbnail, name='update_thumbnail'),
    url(r'^nullable_check/$', services_views.check_nullable, name='check_nullable'),
    
    url(r'^service_url_list/$', services_views.service_url_list, name='service_url_list'),
    url(r'^service_url_add/$', services_views.service_url_add, name='service_url_add'),
    url(r'^service_url_delete/(?P<svid>\d+)/$', services_views.service_url_delete, name='service_url_delete'),
    url(r'^service_url_update/(?P<svid>[0-9]+)/$', services_views.service_url_update, name='service_url_update'),
    url(r'^test_connection/$', services_views.test_connection, name='test_connection'),
    url(r'^register_action/$', services_views.register_action, name='register_action'),
    url(r'^db_field_delete/$', services_views.db_field_delete, name='db_field_delete'),
    #url(r'^db_field_changetype/$', services_views.db_field_changetype, name='db_field_changetype'),
    url(r'^db_field_rename/$', services_views.db_field_rename, name='db_field_rename'),
    url(r'^db_field_add/$', services_views.db_add_field, name='db_field_add'),
]