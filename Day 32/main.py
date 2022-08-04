import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.weekday()
file = open("quotes.txt")
quotes = file.readlines()
my_email = 'deepthroat2580@gmail.com'
password = 'incrediblehulk2'

if now.weekday() == day:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # or use the normal one ie file= smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="apurvkrishna0411@gmail.com", msg=f"Subject:Hello\n\n {random.choice(quotes)}")


file.close()


