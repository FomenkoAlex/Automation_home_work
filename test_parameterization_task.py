import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  фикстура инициализации и закрытия браузера
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome() #  запускаем браузер
    browser.implicitly_wait(5) # проверяем максимум 5 сек. можем ли приступить к выполнению команды
    yield browser #  ждем выполнения всего теста
    browser.quit() #  закрываем браузер

#  создаем параметры, которые будем менять для запуска каждого теста
@pytest.mark.parametrize("url", ["https://stepik.org/lesson/236895/step/1",
                                 "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1",
                                 "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1",
                                 "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1",
                                 "https://stepik.org/lesson/236905/step/1"])
def test_alien(browser, url):
    browser.get(url)
    answer = str(math.log(int(time.time()))) #  считаем ответ для задания
    browser.find_element(By.TAG_NAME, "textarea").send_keys(answer) #  находим поле для ввода ответа и сразу записываем
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
    #  находим кнопку и ждем пока она станет кликабельной
    button.click() #  жмем на кнопку
    check_results = browser.find_element(By.CLASS_NAME, "smart-hints__hint") #  находим елемент где хранится ответ
    assert "Correct!" in check_results.text #  сравниваем ответ с корректным

if __name__ == "__main__":
    pytest.main()