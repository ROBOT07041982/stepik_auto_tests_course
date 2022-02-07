import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#открываем ссылку
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome(options=options)
browser.get(link)

#счтьываем Х
x_element=browser.find_element(By.CSS_SELECTOR, "#input_value")
x=int(x_element.text)

#считаем функцию
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
y=calc(x)

#заполняем ответ
answer=browser.find_element(By.ID, "answer")
answer.send_keys(y)

#скроллим до кнопки
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#ыбираем чекбокс и радиобаттон
option1=browser.find_element(By.ID, "robotCheckbox")
option1.click()
option2=browser.find_element(By.ID, "robotsRule")
option2.click()

#нажимаем кнопку подтверждения
browser.find_element(By.TAG_NAME, "button").click()
