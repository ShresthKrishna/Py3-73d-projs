import requests
from datetime import datetime
parameters = {
    'lat': 24.108456,
    'lng': 83.677391,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json?lat=24.108456&lng=83.677391", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]['sunrise'].split("T")[1].split(":")[0]
sunset = data["results"]['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(datetime.now().time())