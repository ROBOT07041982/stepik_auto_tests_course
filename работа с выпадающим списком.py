import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    #открываем страницу в браузере
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    #считаем правильный ответ
    NUM1=browser.find_element(By.ID, "num1")
    num1=int(NUM1.text)

    NUM2=browser.find_element(By.ID, "num2")
    num2=int(NUM2.text)

    SUM=num1+num2

    #кликаем на выпадающий список
    browser.find_element(By.ID, "dropdown").click()

    #кликаем правильный ответ
    browser.find_element(By.CSS_SELECTOR, f'[value="{SUM}"]').click()

    #нажимаем подтверждение
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
