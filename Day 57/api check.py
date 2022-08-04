import requests
URL = "https://api.agify.io"
para = {
    "name":"Shresth"
}
response = requests.get(url=URL, params=para).json()
gender = requests.get(url=f'https://api.genderize.io?name=shresth').json()['gender']
print(response)
print(gender)