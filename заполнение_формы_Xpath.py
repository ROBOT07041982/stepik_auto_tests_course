import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("http://suninjuly.github.io/find_xpath_form")
input1 = driver.find_element(By.TAG_NAME, "input")
input1.send_keys("Dmitrii")
input2 = driver.find_element(By.NAME, "last_name")
input2.send_keys("Ragimov")
input3 = driver.find_element(By.CSS_SELECTOR, ".form-control.city")
input3.send_keys("Tyumen")
input4 = driver.find_element(By.CSS_SELECTOR, "#country")
input4.send_keys("Russia")
button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
button.click()


time.sleep(10)
driver.quit()
