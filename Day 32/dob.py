
import pandas
import smtplib
import random
import datetime as dt

details = pandas.read_csv("birthdays.csv")
my_email = 'deepthroat2580@gmail.com'
password = 'incrediblehulk2'
date = dt.datetime.now()
day_val = date.day
month_val = date.month
year = date.year
names = details.name

with open("./letter_templates/letter_1.txt") as file:
    letter_1 = file.readlines()
with open("./letter_templates/letter_2.txt") as file:
    letter_2 = file.readlines()
with open("./letter_templates/letter_3.txt") as file:
    letter_3 = file.readlines()

dob = pandas.DataFrame(details)
dob = dob.to_dict(orient='records')
for i in dob:
    if i['day'] == day_val and i['month'] == month_val:
        letters = [letter_3, letter_2, letter_1]
        x = random.choice(letters)
        x = [y.replace('[NAME]', f"{i['name']}") for y in x]
        wish=''
        for j in x:
            wish += j

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=i['email'], msg=f"Subject: Happy Birthday \n\n{wish}")






