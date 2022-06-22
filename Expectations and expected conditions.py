from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"  # ссылка на тестируемую страницу
    browser.get(link)  # открываем страницу

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    # здесь мы ждем пока в определенном елементе не будет такой текст который нам нужен, ждем максимум 12 сек

    button = browser.find_element(By.ID, "book")  # находим кнопку
    button.click()  # нажимаем кнопку

    x_element = browser.find_element(By.ID, "input_value")  # берем значение Х
    x = x_element.text  # сохраняем значение Х в переменную
    y = calc(x)  # профодим расчет по формуле, которую указали выше в функции

    input1 = browser.find_element(By.ID, "answer")  # находим поле для ввода
    input1.send_keys(y)  # вводим значение расчета в поле

    button1 = browser.find_element(By.ID, "solve")  # находим кнопку
    button1.click()  # нажимаем на кнопку

finally:
    time.sleep(10)  # подождать 5 сек, забрать результат
    browser.quit()  # закрываем браузер после всех манипуляций
