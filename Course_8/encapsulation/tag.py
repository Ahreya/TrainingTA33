import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
--- find element by tag ---
"""
chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://the-internet.herokuapp.com")

# maximizam fereastra
chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
time.sleep(2)

# find elements with tag input and store them in a list
input_list = chrome.find_elements(By.TAG_NAME, "input")

# use the list to fill the username and password
input_list[0].send_keys("tomsmith")
time.sleep(1)
input_list[1].send_keys("SuperSecretPassword!")
time.sleep(1)

# click on Login button
chrome.find_element(By.TAG_NAME, "i").click()
time.sleep(2)



