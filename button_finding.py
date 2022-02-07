from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

#browser = webdriver.Chrome()
browser.get("http://google.ru")
#button = browser.find_element_by_css_selector(".gN089b")

browser.quit()