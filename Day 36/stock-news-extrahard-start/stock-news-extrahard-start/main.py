import requests
from itertools import islice
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
UP = "🔺"
DOWN = "🔻"
#Alpha
API_KEY = "A74EEY9NNAA17H8N"
ALPHA_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&interval=60min&apikey={API_KEY}"

#NEWS
NEWS_API = "55b6a6c3dafc4e818c17c9cf694d35d6"
NEWS_URL = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2021-06-24&sortBy=popularity&apiKey={NEWS_API}"

#SMS
account_sid = "AC7d10ee5f0cf148c3b4c5b37bbbee5328"
auth_token = "e3a0d00c9eda4b72950b0acec1806f13"
api_key = "140cf6d037b152bf926f8897a98c774b"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def news(sign,change,title, desc):
    print(f"TSLA: {sign}{change}")
    headline = ''
    for i in range(3):
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"TSLA: {sign}{change}"
                 f"\nHeadline: {title[i]}"
                  f"\nBrief: {desc[i]}",
            from_='+15109453241',
            to='+916203859697'
        )

calendar = dt.datetime.now()
day = calendar.date().today()
yesterday = day - dt.timedelta(days=2)
bef_yesterday = day - dt.timedelta(days=3)


response = requests.get(ALPHA_URL)
data_1 = float(response.json()['Time Series (Daily)'][f"{yesterday}"]['1. open'])
data_2 = float(response.json()['Time Series (Daily)'][f"{bef_yesterday}"]["4. close"])

news_response = requests.get(NEWS_URL)
title = []
desc = []
for i in range(3):
    title.append(news_response.json()["articles"][i]["title"])
    desc.append(news_response.json()["articles"][i]["description"])



raise_percent = ((data_1-data_2)*100)/data_2
# if int(raise_percent) < -5 or int(raise_percent)> 5
if int(raise_percent) in range(-5,5):
    if raise_percent < 0:
        fall_percentage = -1*raise_percent
        news(DOWN,round(fall_percentage,2),title,desc)
    else:
        news(UP,round(raise_percent,2),title,desc)

else:
    print("No significant change")




