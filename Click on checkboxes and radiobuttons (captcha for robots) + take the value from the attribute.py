from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/get_attribute.html" # ссылка на тестируемую страницу
    browser.get(link) # открываем страницу

    x_element = browser.find_element(By.TAG_NAME, "img") # находим элемент
    x = x_element.get_attribute("valuex") # берем значение с атрибута
    y = calc(x) # проводим рассчет

    add_answer = browser.find_element(By.ID, value="answer") # находим поле для ответа
    add_answer.send_keys(y) # записываем значение рассчитаное выше в поле
    checkBox = browser.find_element(By.ID, value="robotCheckbox") # поиск чекбокса
    checkBox.click() # выбираем чекбокс
    radioButton = browser.find_element(By.ID, value="robotsRule") # поиск переключателя
    radioButton.click() # выбираем переключатель
    button = browser.find_element(By.CLASS_NAME, value="btn") # находим кнопку
    button.click() # нажимаем на кнопку

finally:
    time.sleep(10)  # подождать 5 сек, забрать результат
    browser.quit() # закрываем браузер после всех манипуляций
