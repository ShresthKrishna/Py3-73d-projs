from selenium import webdriver
from selenium import common
import time
import requests
from bs4 import BeautifulSoup


location = "E:\devep\chromedriver.exe"


response = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.51273573828125%2C%22east%22%3A-121.35392226171875%2C%22south%22%3A37.48708129572077%2C%22north%22%3A38.06238242908446%7D%2C%22mapZoom%22%3A9%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D", headers={'User-Agent': 'Mozilla/5.0'})
zillow = response.text
soup = BeautifulSoup(zillow,'html.parser')
props = soup.select(".list-card-top a")

# To get property links
links = []
for link in props:
    href = link['href']
    print(href)
    if 'https://' not in href:
        links.append(f'https://www.zillow.com/{href}')
    else:
        links.append(href)


# To get prices of the properrty
all_prices = []
prices = soup.select("div .list-card-price")
for i in prices:
    price = i.get_text().split('/')[0]
    print(price)
    all_prices.append(price)


# To get address of property
all_address = []

address = soup.select(".list-card-addr")
for address in address:
    addresses = address.get_text()
    print(addresses)
    all_address.append(addresses)


driver = webdriver.Chrome(executable_path=location)
if input("wanna open form?")=='y':
    #loop for opening forms
    for i in range(len(links)):
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScv5O-YXb9mUPuys4B6K9nn6hvGZKpRZb1eXxIVtQbazyvE0w/viewform?usp=sf_link")
        time.sleep(2)
        # input address in the form
        add_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        add_input.send_keys(all_address[i])

        # input price in the form
        price_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_input.send_keys(all_prices[i])

        # input links in the form
        link_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_input.send_keys(links[i])

        # To submit
        submit = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div/div/span/span").click()
        time.sleep(1)