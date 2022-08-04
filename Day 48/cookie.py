import random
import time
import operator

import selenium.common.exceptions
from selenium import webdriver


timeout = time.time() + 5
time_limit = time.time() + 60*5
chrome_driver_location = "E:\devep\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
items_id = [items.get_attribute("id") for items in items]

while True:
    cookie.click()
    curtime = time.time()
    if time.time() > timeout:
        money = int(driver.find_element_by_id("money").text.replace(",",''))

        # the prices for all items
        prices = [i.text.split('-')[1].strip() for i in driver.find_elements_by_css_selector("#store b") if i.text!='']
        prices = [int(j.replace(',','')) for j in prices]

        # item ids and their price
        price_det = {}
        for i in range(len(prices)):
            price_det[items_id[i]] = prices[i]
        print(price_det)

        # things i can afford
        try:
            affordables = {}
            for id, cost in price_det.items():
                if money >= cost:
                    affordables[id] = cost
            print(f"affordables = {affordables}")
            highest_cost_id = max(affordables, key=affordables.get)
            print(highest_cost_id)
            highest_cost = affordables[highest_cost_id]
            driver.find_element_by_id(highest_cost_id).click()
        except ValueError:
            print("Broke as hell")
            pass
        timeout = time.time() + 6
    if time.time() > time_limit:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break


# print(products)
driver.quit()
