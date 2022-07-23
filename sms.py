import os
from twilio.rest import Client

def alert():
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']='AC4aa28d0bdb50b4c59e5f5fce5b16733e'
    auth_token = os.environ['TWILIO_AUTH_TOKEN']='d2acf389726e71d0ff11420b29f9f632'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Alert for an intruder",
                     from_='+19475003564',
                     to='+923170589788'
                 )

    print(message.sid)