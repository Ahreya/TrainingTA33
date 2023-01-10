import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
link text = textul care este pus peste un link
linkurile pe un site sunt definite prin intermediul unei ancore (tag-ul a)
un element de tip ancora are urmatoarele componente:
- tag-ul de inceput <a>
- link-ul catre care se va face navigarea (href = "valoare")
- textul care este afisat peste link (linktext)
- tag-ul de sfarsit </a>
"""

chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://the-internet.herokuapp.com")

# maximizam fereastra
chrome.maximize_window()
time.sleep(2)

# accesam pagina Checkboxes
chrome.find_element(By.LINK_TEXT, "Checkboxes").click()
time.sleep(2)
chrome.back()
chrome.find_element(By.LINK_TEXT, "Form Authentication").click()
time.sleep(2)


