from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#открываем ссылку
browser = webdriver.Chrome(options=options)
browser.get("http://suninjuly.github.io/file_input.html")

#заполняем поля
browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys(111)
browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys(222)
browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys(333)

#выбираем файл
browser.find_element(By.ID, "file").send_keys("C:/Python/1.txt")

#нажимаем подтверждение
browser.find_element(By.TAG_NAME, "button").click()

