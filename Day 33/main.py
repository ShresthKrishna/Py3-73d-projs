import requests
from datetime import datetime
import smtplib
from tkinter import *
MY_LAT = 24.108456 # Your latitude
MY_LONG = 83.677391 # Your longitude

MY_MAIL = "deepthroat2580@gmail.com"
MY_PASSWORD = "incrediblehulk2"

window = Tk()
def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (int(iss_latitude - MY_LAT) in range(-5, 5) or int(iss_longitude - MY_LONG) in range(-5, 5)):
        return True
# Your position is within +5 or -5 degrees of the ISS position.
def check_time():
    if cur_time >= sunset and cur_time <= sunrise:
        return True
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


time_now = datetime.now()
cur_time = int(time_now.strftime("%H"))


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


while True:
    if check_time() and check_pos():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
            connect.starttls()
            connect.login(user=MY_MAIL, password=MY_PASSWORD)
            connect.sendmail(from_addr=MY_MAIL, to_addrs="deepthroat2580@yahoo.com", msg="Look Above You as ISS is passing through")
            print("see mail")
    else:
        print("Sorry, ISS won't be visible right now")


    window.after(60000)
window.mainloop()