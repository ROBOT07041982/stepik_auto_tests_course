import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(options=options)
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
    input1.send_keys("Dmitrii")
    input2 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[1]/div[2]/input")
    input2.send_keys("11111111")
    input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
    input3.send_keys("lhfvklshfvlksdfhl")
   
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
