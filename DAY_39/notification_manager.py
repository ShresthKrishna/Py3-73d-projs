import requests
from twilio.rest import Client
SID = "AC7d10ee5f0cf148c3b4c5b37bbbee5328"
AUTH = "e3a0d00c9eda4b72950b0acec1806f13"
FROM = "+15109453241"
TO = "+916203859697"
class NotificationManager:
    def send_sms(self,message):
#This class is responsible for sending notifications with the deal flight details.
        account_sid = SID
        auth_token = AUTH
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=message,
            from_=FROM,
            to=TO
        )
