from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():  # первый тестСьюит

    @classmethod  # создаем функцию инициализации браузера, оборачиваем в декоратор, будет применяться один раз на весь
                  # класс
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod  # создаем функцию закрытия браузера, оборачиваем в декоратор, будет применяться один раз на весь
                  # класс
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():  # второй тестСьюит

    def setup_method(self):  # создаем функцию инициализации браузера, не оборачиваем в декоратор, будет применяться
                             # к каждому тесту по отдельности в классе
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):# создаем функцию закрытия браузера, не оборачиваем в декоратор, будет применяться
                              # к каждому тесту по отдельности в классе
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# запускаем в терминале командой pytest -s test_fixture1.py параметр -s позволяет увидеть вывод print()
