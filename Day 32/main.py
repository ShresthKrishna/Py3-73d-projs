import smtplib
import datetime as dt
import random
import os
now = dt.datetime.now()
day = now.weekday()
file = open("quotes.txt")
quotes = file.readlines()
my_email = os.environ['FUN_MAIL']
password = os.environ['PASS']

if now.weekday() == day:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # or use the normal one ie file= smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Hello\n\n {random.choice(quotes)}")


file.close()


