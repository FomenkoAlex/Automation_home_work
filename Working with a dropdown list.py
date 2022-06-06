from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"  # ссылка на тестируемую страницу
    browser.get(link) # открываем страницу

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Alex")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Fomenko")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@mail.com")
    down_file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    down_file.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, value="btn")  # находим кнопку
    button.click()  # нажимаем на кнопку

finally:
    time.sleep(10)  # подождать 5 сек, забрать результат
    browser.quit()  # закрываем браузер после всех манипуляций
