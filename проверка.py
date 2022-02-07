import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#открываем ссылку
link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome(options=options)
browser.get(link)

browser.find_element(By.ID, "button")