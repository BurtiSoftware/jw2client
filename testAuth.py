from JwtService import JwtService
import os

def getKeys():
    private = os.environ['priv_key_path']
    with open(private, "rb") as pem_file:
        JWT_PRIVATE_KEY = pem_file.read()

    public = os.environ['pub_key_path']
    with open(public, "rb") as pem_file:
        JWT_PUBLIC_KEY = pem_file.read()

    return JWT_PRIVATE_KEY, JWT_PUBLIC_KEY

keys = getKeys()
JWT_PRIVATE_KEY, JWT_PUBLIC_KEY = keys
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

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZXYuY29yZS5qdzIudmF0aS5yb2Nrc1wvIiwiYXVkIjoiaHR0cDpcL1wvZGV2LmNvcmUuancyLnZhdGkucm9ja3NcLyIsImV4cCI6MTY5MTc5OTQxMCwiZGF0YSI6eyJ1c2Vyc19pZCI6MywidGVuYW50X2lkIjoxLCJuYW1lIjoiYWRtaW4iLCJsb2dpbiI6ImFkbWluIiwiZW1haWwiOiJhZG1pbkBlbWFpbC5jb20iLCJhdmF0YXJfdXJsIjoiaHR0cHM6XC9cL2F2YXRhcnMuZ2l0aHVidXNlcmNvbnRlbnQuY29tXC91XC80NjM4MzQ2NT9zPTQwJnY9NCIsImFjdGl2ZSI6dHJ1ZSwibWFzdGVyIjpmYWxzZSwicmVzZXRfcHdkIjpmYWxzZSwiZ3JvdXBzIjpbeyJ1c2VyX2dyb3VwX2lkIjoyLCJjb21wYW55X2lkIjo0LCJtYW5hZ2VyIjpmYWxzZX0seyJ1c2VyX2dyb3VwX2lkIjoxMSwiY29tcGFueV9pZCI6NCwibWFuYWdlciI6dHJ1ZX0seyJ1c2VyX2dyb3VwX2lkIjoxLCJjb21wYW55X2lkIjoxLCJtYW5hZ2VyIjp0cnVlfV0sImFkbWlucyI6W3sidGVuYW50X2lkIjoxfSx7InRlbmFudF9pZCI6Mn1dLCJleHRlcm5hbF9hY2NvdW50cyI6W119fQ.PO8Jkzp69mvIRThMm0Mur-Wmo_rjjcNfj1fJf4fnopbNMSdsoO2HwRZTSyHYgo2kMxakr106SPuBDmdwfUXLefV5d8z4mk-931HvXZ-f8m2C7wn9XGcfJVXA8CKWxV5fpj8Gv3Wn4FsS0vcq7fEhNfLIAqqPNo7-17P1ZC_ShzA'
jwt = JwtService(JWT_PRIVATE_KEY, JWT_PUBLIC_KEY, payload, JWT_EXPIRATION)
applicationToken = jwt.generate_application_token(token)

print(applicationToken)
