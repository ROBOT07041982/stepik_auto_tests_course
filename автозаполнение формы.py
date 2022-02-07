from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Dmitrii")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Ragimov")
    input3 = browser.find_element_by_css_selector(".form-control.city")
    input3.send_keys("Tyumen")
    input4 = browser.find_element_by_css_selector("#country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
