import os
from twilio.rest import Client

def alert():
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']='AC4a51e3aa7b1905fd552324e5fa113e49'
    auth_token = os.environ['TWILIO_AUTH_TOKEN']='9015e90cc30ef7927d793e3e48ab608b'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Alert for an intruder",
                     from_='+19475003564',
                     to='+923170589788'
                 )

    print(message.sid)
