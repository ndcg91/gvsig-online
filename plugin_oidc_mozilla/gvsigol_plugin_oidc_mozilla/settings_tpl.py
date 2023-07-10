GVSIGOL_AUTH_BACKEND = '##GVSIGOL_AUTH_BACKEND##'
OIDC_OP_BASE_URL = '##OIDC_OP_BASE_URL##'
OIDC_OP_REALM_NAME = '##OIDC_OP_REALM_NAME##'
OIDC_RP_CLIENT_ID = '##OIDC_RP_CLIENT_ID##'
OIDC_RP_CLIENT_SECRET = '##OIDC_RP_CLIENT_SECRET##'
OIDC_OP_AUTHORIZATION_ENDPOINT = "##OIDC_OP_AUTHORIZATION_ENDPOINT##"
OIDC_OP_TOKEN_ENDPOINT = "##OIDC_OP_TOKEN_ENDPOINT##"
OIDC_OP_USER_ENDPOINT = "##OIDC_OP_USER_ENDPOINT##"
OIDC_OP_JWKS_ENDPOINT = "##OIDC_OP_JWKS_ENDPOINT##"
OIDC_OP_LOGOUT_ENDPOINT = "##OIDC_OP_LOGOUT_ENDPOINT##"
OIDC_OP_LOGOUT_URL_METHOD = GVSIGOL_AUTH_BACKEND + ".provider_logout"
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_STORE_ACCESS_TOKEN = True
OIDC_STORE_ID_TOKEN = True
OIDC_RP_SCOPES = 'openid email username geoserver-client'
KEYCLOAK_ADMIN_CLIENT_ID = '##KEYCLOAK_ADMIN_CLIENT_ID##'
KEYCLOAK_ADMIN_CLIENT_SECRET = '##KEYCLOAK_ADMIN_CLIENT_SECRET##'
MANAGE_PASSWORD_URL = '##MANAGE_PASSWORD_URL##'
OIDC_EXEMPT_URLS = ['gvsigol_authenticate_user', 'gvsigol_logout_user']
LOGIN_REDIRECT_URL_FAILURE = 'index'