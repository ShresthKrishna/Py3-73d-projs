from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_location = "E:\devep\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_location)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# count = driver.find_element_by_css_selector("#articlecount a")
# print(count.text)
# # count.click()
#
# all_portals = driver.find_element_by_link_text("All portals")
# # all_portals.click()
#
# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("shahrukh khan")
# # submit = driver.find_element_by_name("go")
# # submit.click()
# # search_bar.send_keys(Keys.ENTER)
# time.sleep(10)
# # driver.quit()

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Shresth Krishna")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Sinha")
mail = driver.find_element_by_name("email")
mail.send_keys("helloworld@gmail.com")
submit = driver.find_element_by_class_name("btn-block")
submit.click()