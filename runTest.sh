#!/bin/bash

export JW2_CORE_URL="http://core_api"
export JW2_CONTENT_URL="http://content_api"
export JW2_RENDITION_AUTH='{"user":"admin@email.com","password":"admin"}'

echo "JW2_CORE_URL: $JW2_CORE_URL"
echo "JW2_CONTENT_URL: $JW2_CONTENT_URL"

export application_instance_id=1
export application_id=1
export application_instance_title="Content 1"
export access_url="http://mysite.info"

export priv_key_path="-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgEj3uJPmPOcmulkYPpCeoDebTuC+M2B6S6ER/RD9glWJJm6FCO0e
Ru17y52yYVO/vipPiUppLuu/0K8DTRQoTZS/foHV6o2yKx/nkTNzGR0nbJC3mjZx
cPwFO57XO+h+tzslKyqNq5FHE4kVc3u+ELd8DYG57vRPNEzNknHnp8OtAgMBAAEC
gYADfCFKnwJln8nim2/RhGHuhfJcdXkKsIyQIsXNW+4vm59ERAJLINkOWo08+NoB
H/U7HBVYgnGFPOIAmc3CmrIpzXEhlE2mqZAXY4WiVd7Y1saAJt/5kvX+RTxbuo+q
qf7c5ysvIjrCcsnPH6xVJSWU3cR/7cloregS79Lfj1s+2QJBAI/ExMdBNcKvfI6S
gOGiyc23C37Dn+obK8KUVH1xDjSQVLYLGRqggRa3Cl37xfvsryKBndeQ/1pIuk+o
QUu2WtMCQQCB7dYhiTQDNtt8kkG9Xji30hIdLuIwWNIfbsbsFLCa1bEa4BWWOKVo
xlZa7UF/LYTi1yk3zx1qoowe5DAZgVd/AkAGvBLzuoxIKGxPSXGcIEIPzulM8OEG
2Gr+XHBwx+EAeVpehLqSUr55T+2+ZVLq8DVsCmJYfMRZeFqx7JHSeCJdAkAzoYqV
GwujN1pzHz+me9m4Gm9+T1Is+i7NtNyxles0LDTLxD5vyqTYhPBuA5gibLlA11WW
yuQaqutZnz4J9J8LAkBRzO3vZdO+303N7GJsTV813EKEkruGf3hJqg0H7Up/6qqL
FMO2zY4A2R+Vjy0HBQptVk1V6AAigv/q/5/U49/L
-----END RSA PRIVATE KEY-----"

export pub_key_path="-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgEj3uJPmPOcmulkYPpCeoDebTuC+
M2B6S6ER/RD9glWJJm6FCO0eRu17y52yYVO/vipPiUppLuu/0K8DTRQoTZS/foHV
6o2yKx/nkTNzGR0nbJC3mjZxcPwFO57XO+h+tzslKyqNq5FHE4kVc3u+ELd8DYG5
7vRPNEzNknHnp8OtAgMBAAE=
-----END PUBLIC KEY-----"

export JWT_ISSUER='http://dev.core.jw2.vati.rocks/'
export JWT_AUDIENCE='http://dev.core.jw2.vati.rocks/'
export JWT_EXPIRATION=10000


python3 testAuth.py