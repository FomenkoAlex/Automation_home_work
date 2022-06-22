from selenium import webdriver
import time

link = " http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    # переходим по ссылке
    browser.get(link)

    # находим кааждое поле и заполняем его
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Fomenko")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Kharkiv")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Ukraina")
    # находим кнопку с помощью xpath
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    # кликаем на кнопку
    button.click()

finally:
    # ждем 30 сек
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
