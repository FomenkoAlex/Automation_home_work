from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

def test_one_registry_pass():
    browser = webdriver.Chrome()
    try:
        # ссылка для теста
        link = "http://suninjuly.github.io/registration1.html"

        browser.get(link)

        # ввод данных в поля
        input1 = browser.find_element(By.XPATH, value="//div[@class='first_block']//input")
        input1.send_keys("Alex")
        input2 = browser.find_element(By.XPATH, value="//div[@class='first_block']//div[2]//input")
        input2.send_keys("Fomenko")
        input3 = browser.find_element(By.XPATH, value="//div[@class='first_block']//div[3]//input")
        input3.send_keys("mail@test.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

def test_one_registry_failed():
    browser = webdriver.Chrome()
    try:
        # ссылка для теста
        link = "http://suninjuly.github.io/registration2.html"

        browser.get(link)

        # ввод данных в поля
        input1 = browser.find_element(By.XPATH, value="//div[@class='first_block']//input")
        input1.send_keys("Alex")
        input2 = browser.find_element(By.XPATH, value="//div[@class='first_block']//div[2]//input")
        input2.send_keys("Fomenko")
        input3 = browser.find_element(By.XPATH, value="//div[@class='first_block']//div[3]//input")
        input3.send_keys("mail@test.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, value="button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, value="h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()



if __name__ == "__main__":
    pytest.main()
