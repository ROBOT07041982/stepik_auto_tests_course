import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.get("http://suninjuly.github.io/find_link_text")
a=str(math.ceil(math.pow(math.pi, math.e)*10000))
#print(a)
link = driver.find_element(By.LINK_TEXT, a)
link.click()

input1 = driver.find_element_by_tag_name("input")
input1.send_keys("Dmitrii")
input2 = driver.find_element_by_name("last_name")
input2.send_keys("Ragimov")
input3 = driver.find_element_by_css_selector(".form-control.city")
input3.send_keys("Tyumen")
input4 = driver.find_element_by_css_selector("#country")
input4.send_keys("Russia")
button = driver.find_element_by_css_selector("button.btn")
button.click()


time.sleep(10)
driver.quit()
