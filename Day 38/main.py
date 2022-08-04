import requests
import datetime as dt
APP_ID = "0a31711c"
API_KEY = "f0317f217efebbb36364883fae8a0355"
TRACER_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/70dd7c7ed02c78186d7034a1219a927f/copyOfMyWorkouts/workouts"
header = {
    "Content-Type":"application/json"
}
headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    # "x-remote-user-id": "0",
    # "content-type": "application/json",
}
exercise_t = input("What u did today: ")
body = {
 "query": exercise_t ,
 "gender": "female",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 30
}
datea = dt.datetime.now()
date = datea.strftime("%d/%m/%Y")
time = datea.strftime("%H:%M:%S")

response = requests.post(url=TRACER_URL,json=body,headers=headers)
exercise = response.json()
print(exercise)
details = {
    "workout":{
        "date":f"{date}",
        'time':f"{time}",
        'exercise': f'{response.json()["exercises"][0]["user_input"]}',
        'duration': f'{response.json()["exercises"][0]["duration_min"]}',
        'calories': f'{response.json()["exercises"][0]["nf_calories"]}',
        'id':'2'
    }
}
sheety = requests.post(url=SHEETY_URL,json=details, headers=header)
print(sheety.json())

