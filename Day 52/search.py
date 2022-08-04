from selenium import webdriver
from selenium import common
import time

SCROLL_PAUSE_TIME = 1
SIMILAR = 'chefsteps'
PROMISED_SPEED_DOWN = 150
MAIL = "allhailprincevegeta@gmail.com"
PASS = "incrediblehulk2"
class Instafollower():
    def __init__(self):
        self.driver_location = "E:\devep\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.driver_location)
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

    def login(self):
        self.driver.find_element_by_name("username").send_keys(MAIL)
        self.driver.find_element_by_name("password").send_keys(PASS)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        except common.exceptions.NoSuchElementException:
            pass

    def find_followers(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(SIMILAR)
        time.sleep(2)
        self.driver.find_element_by_class_name("-qQT3").click()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text("follower").click()
        self.driver.find_elements_by_partial_link_text("Follow")
        time.sleep(2)


        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(last_height):
            scr1 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", las)
            time.sleep(2)

