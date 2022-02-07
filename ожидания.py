import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#открываем ссылку
browser = webdriver.Chrome(options=options)

# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


#проверять цену в течинии  5 сек пока она не станет 100  нажимаем кнопку бук
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(By.ID, "book").click()

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
browser.find_element(By.ID, "solve").click()

