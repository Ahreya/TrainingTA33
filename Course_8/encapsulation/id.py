import time
from selenium import webdriver
from selenium.webdriver.common.by import By

###### find element by id ######

chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.maximize_window()
# first we have to go to the site we want
chrome.get("https://wiki.ubuntu.com")
time.sleep(2)

# mergem in casuta de search si cautam ceva
chrome.find_element(By.ID, "searchinput").send_keys("xerus")
time.sleep(2)
chrome.find_element(By.ID, "titlesearch").click()
time.sleep(2)


