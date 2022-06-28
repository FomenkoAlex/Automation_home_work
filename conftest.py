import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

#  функция которарая обрабатыет опции
# def pytest_addoption(parser):
#     parser.addoption('--browser_name', action='store', default=None,
#                      help="Choose browser: chrome or firefox")

#  фикстура позволяющая пользоваться разным браузером для тестов, фикстура передает в опции данные, которые
#  обрабатывает функция выше
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     browser = None
#     if browser_name == "chrome":
#         browser = webdriver.Chrome()
#     elif browser_name == "firefox":
#         browser = webdriver.Firefox()
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     browser.quit()

#  при запуске файла с тестами, нужно обязательно указать параметр --browser_name=название браузера
#  иначе будет ошибка _pytest.config.UsageError: --browser_name should be chrome or firefox

#  Если в функции обработчике опций в default выставить одно из названий браузера, то тесты будут запускаться
#  на нем автоматически и можно будет запускать файл с тестами без параметра, но при необходимости
#  выбора другого браузера нужно будет указать его в параметрах при запуске

#  в этом файле мы записываем часто вызываемые фикстуры, для того что б не прописывать их в каждом файле с тестами
