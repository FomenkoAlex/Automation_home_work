from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"  # ссылка на тестируемую страницу
    browser.get(link) # открываем страницу

    button1 = browser.find_element(By.CLASS_NAME, value="btn")  # находим кнопку
    button1.click()  # нажимаем на кнопку

    alert = browser.switch_to.alert  # переключаем фокус на всплывающее уведомление(алерт)
    alert.accept()  # нажимаем ОК на всплывающем уведомлении
    x_element = browser.find_element(By.ID, "input_value")  # берем значение Х
    x = x_element.text  # сохраняем значение Х в переменную
    y = calc(x)  # профодим расчет по формуле, которую указали выше в функции

    input1 = browser.find_element(By.ID, "answer")  # находим поле для ввода
    input1.send_keys(y)  # вводим значение расчета в поле

    button = browser.find_element(By.CLASS_NAME, value="btn")  # находим кнопку
    button.click()  # нажимаем на кнопку

finally:
    time.sleep(10)  # подождать 5 сек, забрать результат
    browser.quit()  # закрываем браузер после всех манипуляций
