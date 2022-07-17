# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# TWILIO_ACCOUNT_SID = 'ACe6c027f52a2cca5fc347c47e18c2209a'
# TWILIO_AUTH_TOKEN = 'be915f498b2b39156cd26b40322bf736'
account_sid = 'ACe6c027f52a2cca5fc347c47e18c2209a'
auth_token = 'be915f498b2b39156cd26b40322bf736'
client = Client(account_sid, auth_token)

message = client.messages.create(
         from_ = '+19786435004',
         body='Do you knon Cho Him ? - He is a dangerous person!',
         to='+84329898862'
     )

print(message.sid)