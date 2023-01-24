from gvsigol.settings import GVSIGOL_AUTH_BACKEND
OIDC_OP_BASE_URL = 'https://keycloak.scolab.eu/auth'
OIDC_OP_REALM_NAME = 'migrate.gvsigonline.com'
OIDC_RP_CLIENT_ID = 'geoserver-client'
OIDC_RP_CLIENT_SECRET = '128b5eda-8cbd-471b-a9cf-826baf322734'
OIDC_OP_AUTHORIZATION_ENDPOINT = "https://keycloak.scolab.eu/auth/realms/migrate.gvsigonline.com/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = "https://keycloak.scolab.eu/auth/realms/migrate.gvsigonline.com/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = "https://keycloak.scolab.eu/auth/realms/migrate.gvsigonline.com/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = "https://keycloak.scolab.eu/auth/realms/migrate.gvsigonline.com/protocol/openid-connect/certs"
OIDC_OP_LOGOUT_ENDPOINT = "https://keycloak.scolab.eu/auth/realms/migrate.gvsigonline.com/protocol/openid-connect/logout"
OIDC_OP_LOGOUT_URL_METHOD = GVSIGOL_AUTH_BACKEND + ".provider_logout"
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_STORE_ACCESS_TOKEN = True
OIDC_STORE_ID_TOKEN = True
OIDC_RP_SCOPES = 'openid email username geoserver-client'


KEYCLOAK_ADMIN_CLIENT_ID = 'gvsigonline-auth-admin'
KEYCLOAK_ADMIN_CLIENT_SECRET = 'af17d120-f91a-4d05-bbae-411e9359ca78'

