import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome()
driver.get("http://yandex.ru")
driver.get("http://google.com")
driver.get("http://mail.ru")
driver.get("http://rambler.ru")
driver.get("http://youtube.ru")
driver.get("http://nalog.ru")


driver.quit()
