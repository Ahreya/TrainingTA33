import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
----- Partial link text ----
la ce il folosim? 
"""

chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://the-internet.herokuapp.com")

# maximizam fereastra
chrome.maximize_window()
time.sleep(2)

chrome.find_element(By.PARTIAL_LINK_TEXT, "Form").click()
# chrome.find_element(By.PARTIAL_LINK_TEXT, "Authentication").click() # va duce catre primul element care are in compozitie "Authentication"
time.sleep(2)
