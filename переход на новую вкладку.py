import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#открываем ссылку
browser = webdriver.Chrome(options=options)
browser.get("http://suninjuly.github.io/redirect_accept.html")

#нажимаем на кнопку
browser.find_element(By.TAG_NAME, "button").click()

#получаем имя новой вкладки
new_window = browser.window_handles[1]

#переходин на новую вкладку
browser.switch_to.window(new_window)

#cчитываем Х
x_element=browser.find_element(By.ID, "input_value")
x=x_element.text

#считаем функцию
def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))
y=calc(x)

#вводим ответ
browser.find_element(By.ID, "answer").send_keys(y)

#нажимаем подтверждение
browser.find_element(By.TAG_NAME, "button").click()