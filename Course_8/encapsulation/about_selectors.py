import time
from selenium import webdriver
from selenium.webdriver.common.by import By
"""
Elementele dintr-un site web sunt identificabile prin intermediul unui tag
Exemple de tag-uri:
- id
- span
- a (ancora)
- td (table data)
- tr (table row)
- ul (unordered list)
- ol (ordered list)
- li (list)
- input
- h (h1, h2, h3, h4, h5, h6) -> h vine de la header(titlu) h1 este cel mai mare si cel mai gros, h6 este cel mai mic
- div (divide)
- p (paragraph)
- etc - o sa le invatati cand o sa aveti nevoie
"""

#### sa identificam niste elemente #####
# ca sa putem lucra cu browserul vom folosi python cu selenium
# ca sa putem lucra cu browserul trebuie sa ii dam o comanda sa se deschida mai intai

chrome = webdriver.Chrome()  # creeaza un nou obiect chrome al clasei Chrome din libraria webdriver
chrome.get("https://www.tutorialspoint.com/index.htm")
#maximizam fereastra
chrome.maximize_window()
time.sleep(2)

