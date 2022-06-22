from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/selects1.html"  # ссылка на тестируемую страницу
    browser.get(link) # открываем страницу

    num1 = browser.find_element(By.ID, "num1")  # находим первое число
    a = num1.text  # запоминаем первое число
    num2 = browser.find_element(By.ID, "num2")  # находим второе число
    b = num2.text  # запоминаем второе число
    summ = int(a) + int(b)  # проводим рассчет
    select = Select(browser.find_element(By.TAG_NAME, "select"))  # находим и раскрываем список
    select.select_by_visible_text(str(summ))  # выбираем значение из списка, то которое лежит в переменной

    button = browser.find_element(By.CLASS_NAME, value="btn")  #  находим кнопку
    button.click()  # нажимаем на кнопку

finally:
    time.sleep(10)  # подождать 5 сек, забрать результат
    browser.quit()  # закрываем браузер после всех манипуляций
