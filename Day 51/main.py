
from selenium import webdriver
import time
PROMISED_SPEED_DOWN = 150
chrome_driver_location = "E:\devep\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get("https://fast.com/")
time.sleep(10)
speed = driver.find_element_by_xpath("//*[@id='speed-value']")
speed_unit = driver.find_element_by_id("speed-units")
print(f"{speed.text} {speed_unit.text}")
driver.quit()