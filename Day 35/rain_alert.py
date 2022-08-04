import requests
from twilio.rest import Client
import os
#tbv5nE1yWRXXYEGRqwM-qEI4UqQ2A2IjcRFm51dD

account_sid = "AC7d10ee5f0cf148c3b4c5b37bbbee5328"
auth_token = "e3a0d00c9eda4b72950b0acec1806f13"
api_key = "140cf6d037b152bf926f8897a98c774b"
parameters={
    "lat": 24.051720,
    "lon": 84.224037,
    "exclude":"current,minutely,daily",
    "appid": api_key
}
data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
data.raise_for_status()
weather = []
for i in range(12):
    weather.append(data.json()["hourly"][i]["weather"][0]["id"])
    if weather[i] < 700:
        value = True

if value:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body = "It's going to rain today keep an umbrella with you.",
        from_='+15109453241',
        to='+916203859697'
    )