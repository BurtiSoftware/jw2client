import jwt
from datetime import datetime, timedelta

class JwtService:
    def __init__(self, private_key, public_key, payload, expiration_time=60):
        self.private_key = private_key
        self.public_key = public_key
        self.payload = payload
        self.expiration_time = expiration_time

    def generate_application_token(self):
        payload_data = self.payload.copy()
        expiration_date = datetime.utcnow() + timedelta(seconds=self.expiration_time)
        payload_data['exp'] = expiration_date.timestamp()
        token = jwt.encode(payload_data, self.private_key, algorithm='RS256')

        return token