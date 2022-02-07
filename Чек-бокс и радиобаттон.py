import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try:
    #открываем страницу в браузере
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    #считывем Х и считаем У
    x_element = browser.find_element(By.ID, "input_value")
    x=x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y=calc(x)

    #вводим ответ
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    #ыбираем чекбокс и радиобаттон
    option1=browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2=browser.find_element(By.ID, "robotsRule")
    option2.click()

    #нажимаем подтверждение
    button=browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
