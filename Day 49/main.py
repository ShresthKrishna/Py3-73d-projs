import time
from selenium import webdriver
from selenium.webdriver.common.by import By

MAIL = 'deepthroat2580@gmail.com'
PASS = 'incrediblehulk2'
chrome_driver_location = "E:\devep\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
log_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
log_in.click()
time.sleep(5)
mail = driver.find_element(By.ID, "username")
mail.send_keys(MAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASS)

sign_in = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
sign_in.click()
