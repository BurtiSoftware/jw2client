#!/bin/bash

export JW2_CORE_URL="http://core_api"
export JW2_CONTENT_URL="http://content_api"

echo "JW2_CORE_URL: $JW2_CORE_URL"
echo "JW2_CONTENT_URL: $JW2_CONTENT_URL"

export application_instance_id=1
export application_id=1
export application_instance_title="Content 1"
export access_url="http://mysite.info"

export JWT_PRIVATE_KEY="YOUR KEY HERE"

export JWT_PUBLIC_KEY="YOUR PUB KEY HERE"

export JWT_ISSUER='http://dev.core.jw2.vati.rocks/'
export JWT_AUDIENCE='http://dev.core.jw2.vati.rocks/'
export JWT_EXPIRATION=10000


python3 testAuth.py