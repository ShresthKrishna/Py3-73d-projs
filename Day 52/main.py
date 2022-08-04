from selenium import webdriver
import time

import tkinter
from search import Instafollower

insta = Instafollower()
insta.login()
insta.find_followers()

