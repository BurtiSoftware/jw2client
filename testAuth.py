from JwtService import JwtService
import os


JWT_PRIVATE_KEY = os.environ['JWT_PRIVATE_KEY']
JWT_PUBLIC_KEY =os.environ['JWT_PUBLIC_KEY']
JWT_ISSUER = os.environ['JWT_ISSUER']
JWT_AUDIENCE = os.environ['JWT_AUDIENCE']
JWT_EXPIRATION = int(os.environ['JWT_EXPIRATION'])

application_instance_id = int(os.environ['application_instance_id'])
application_id = int(os.environ['application_id'])
application_instance_title = os.environ['application_instance_title']
access_url = os.environ['access_url']

applicationData = {
    'application_instance_id': application_instance_id,
    'application_id': application_id,
    'application_instance_title': application_instance_title,
    'access_url': access_url
}

payload = {'iss': JWT_ISSUER, 'aud': JWT_AUDIENCE, 'data': applicationData}

jwt = JwtService(JWT_PRIVATE_KEY, JWT_PUBLIC_KEY, payload, JWT_EXPIRATION)
applicationToken = jwt.generate_application_token()

print("TOKEN")

print(applicationToken)
