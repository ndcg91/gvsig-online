import importlib

try:
    from gvsigol import settings
    auth_backend = importlib.import_module(settings.GVSIGOL_AUTH_BACKEND)
except:
    auth_backend = importlib.import_module('gvsigol_auth.django_auth')

has_group = auth_backend.has_group
has_role = auth_backend.has_role
get_groups = auth_backend.get_groups
get_roles  = auth_backend.get_roles