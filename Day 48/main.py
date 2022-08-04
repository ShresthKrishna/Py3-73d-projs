import random
import time

import selenium.common.exceptions
from selenium import webdriver
chrome_driver_location = "E:\devep\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
money = int(driver.find_element_by_id("money").text)
prices = driver.find_elements_by_css_selector("#store b")
for i in prices:
    i = i.text.split("-")
    print(i[1])
# print(products)
driver.quit()