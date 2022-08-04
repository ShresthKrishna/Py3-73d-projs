from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "allhailprincevegeta@gmail.com"
FB_PASSWORD = "incrediblehulk2"

chrome_driver_path = "E:\devep\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://www.tinder.com")

sleep(2)
accept = driver.find_element(By.XPATH,"//*[@id='s1502865376']/div/div[2]/div/div/div[1]/button")
accept.click()
sleep(1)
login_button = driver.find_element(By.XPATH, "//*[@id='s1502865376']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a")
login_button.click()

sleep(1)
try:
    more_opt = driver.find_element(By.XPATH, "//*[@id='s-225515700']/div/div/div[1]/div/div[3]/span/button")
    more_opt.click()
    fb_login = driver.find_element(By.XPATH,
                                   '//*[@id="s-225515700"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    fb_login.click()
except:
    fb_login = driver.find_element(By.XPATH, '//*[@id="s-225515700"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
fb_allow_window = driver.window_handles[2]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
password = driver.find_element(By.XPATH,'//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(fb_allow_window)
continue_accept = driver.find_element(By.XPATH, "//*[@id='mount_0_0_vt']/div/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div")
continue_accept.click()
print(driver.title)

sleep(10)
allow_location_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.XPATH,".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
