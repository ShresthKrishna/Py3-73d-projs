import pprint

import requests
from bs4 import BeautifulSoup
#upload it to python bot
MAIL = 'deepthroat2580@gmail.com'
PASS = 'incrediblehulk2'
import smtplib
header = {
"Accept-Language":"en-US,en;q=0.9",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
product = requests.get("https://www.amazon.com/Inspiroy-H640P-Graphics-Battery-Free-Sensitivity/dp/B075T6MTJX/ref=sr_1_3?crid=10RCA4I0KQH8B&dchild=1&keywords=drawing+tablet&qid=1625424306&sprefix=drawin%2Caps%2C376&sr=8-3", headers=header)
item = product.text
soup = BeautifulSoup(item, 'html.parser')
item_name = soup.find(name="span", id="productTitle",class_="a-size-large product-title-word-break").get_text()
# print(item_name)
price = soup.find(name="span", id="priceblock_dealprice", class_="a-size-medium a-color-price priceBlockDealPriceString")
print(price)
int_price = float(price.get_text().split("$")[1])
if int_price < 40:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASS)
        connection.sendmail(from_addr=MAIL,
                            to_addrs="deepthroat2580@yahoo.com",
                            msg=f"Subject: Price Fall for {item_name}\n\n"
                                            f"The price for your required "
                                            f"product: {item_name} has fallen to price: ${int_price}."
                                            f" You can purchase it now.")