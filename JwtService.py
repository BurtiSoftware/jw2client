import jwt
import json
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta

class JwtService:
    def __init__(self, private_key, public_key, payload, expiration_time=60):
        self.private_key = private_key
        self.public_key = public_key
        self.payload = payload
        self.expiration_time = expiration_time
        self.validate_payload()

    def encode(self, payload, expiration_date=None):
        payload_data = self.payload.copy()

        if not expiration_date:
            expiration_date = datetime.utcnow() + timedelta(seconds=self.expiration_time)

        payload_data['exp'] = expiration_date.timestamp()
        payload_data['data'] = payload

        token = jwt.encode(payload_data, self.private_key, algorithm='RS256')

        return token

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=['RS256'], audience=self.payload['aud'])
            decoded['data'] = decoded.get('data', {})
        except (InvalidSignatureError, ExpiredSignatureError) as e:
            raise Exception(f"Token error: {str(e)}")
        except (InvalidTokenError, ValueError) as e:
            raise Exception(f"Generic token error: {str(e)}")

        return decoded

    def validate_payload(self):
        required_fields = [
            'application_instance_id',
            'application_id',
            'application_instance_title',
            'access_url'
        ]

        for field in required_fields:
            if field not in self.payload['data']:
                raise TokenCorruptedException('Invalid token ' + field + ' not found')

    def validate_and_decode_token(self, token):
        if not token:
            raise Exception('Token not found')

        try:
            jwt_data = self.decode(token)
        except Exception as e:
            raise e

        if 'data' not in jwt_data:
            raise Exception('Invalid token')

        return jwt_data

    def generate_application_token(self, token):
        app_user = self.get_application_user_from_token(token)

        token = self.encode(app_user)

        return token

    def get_application_user_from_token(self, token):
        jwt = self.validate_and_decode_token(token)
        app_instance_data = self.payload['data']
        app_instance_data['auth_user'] = jwt['data']

        if 'auth_user' in app_instance_data:
            app_instance_data['auth_user'] = self.parse_auth_user(dict(app_instance_data['auth_user']))

        #del app_instance_data['auth_user']['admins']

        return app_instance_data

    def parse_auth_user(self, user_data):
        user_data = json.loads(json.dumps(user_data))
        tenants = user_data.get('admins', [])
        user_data.pop('admins', None)

        groups = user_data.get('groups', [])
        user_data.pop('groups', None)

        external_accs = user_data.get('external_accounts', [])
        user_data.pop('external_accounts', None)

        auth_user = user_data

        auth_admin_col = []

        for tenant in tenants:
            auth_admin = tenant
            auth_admin_col.append(auth_admin)

        auth_user['admins'] = auth_admin_col

        auth_group_col = []

        for group in groups:
            auth_group = group
            auth_group_col.append(auth_group)

        auth_user['groups'] = auth_group_col
        auth_user['external_accounts'] = external_accs

        return auth_user

class TokenNotFoundException(Exception):
    pass

class TokenCorruptedException(Exception):
    pass
