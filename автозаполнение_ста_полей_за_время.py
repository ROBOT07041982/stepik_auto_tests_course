import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("http://suninjuly.github.io/huge_form.html")
elements = driver.find_elements(By.TAG_NAME, "input")
for element in elements:
        element.send_keys("1")

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(30)
driver.quit()
