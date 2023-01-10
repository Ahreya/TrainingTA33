import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
-------- name --------
name este o proprietate pe care o putem folosi
"""

chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://www.seleniumframework.com/Practiceform")

# maximizam fereastra
chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.NAME, "name").send_keys("Takuma Mashimoto")
time.sleep(1)

#cream o lista pentru a lua al doilea e-mail
email_list = chrome.find_elements(By.NAME, "email")
email_list[1].send_keys("takuma.mashimoto@gmail.com")

time.sleep(1)
chrome.find_element(By.NAME, "telephone").send_keys("0752356188")
time.sleep(1)
chrome.find_element(By.NAME, "country").send_keys("Japan")
time.sleep(1)
chrome.find_element(By.NAME, "company").send_keys("Mitsubishi")
time.sleep(1)
chrome.find_element(By.NAME, "message").send_keys("my message is: watashi wa Mashimoto desu.")
time.sleep(2)

# apasam butonul Submit
chrome.find_element(By.LINK_TEXT, "Submit").click()
time.sleep(2)