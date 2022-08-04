from twilio.rest import Client

TWILIO_SID = "AC7d10ee5f0cf148c3b4c5b37bbbee5328"
TWILIO_AUTH_TOKEN = "e3a0d00c9eda4b72950b0acec1806f13"
TWILIO_VIRTUAL_NUMBER = "+15109453241"
TWILIO_VERIFIED_NUMBER = "+916203859697"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
