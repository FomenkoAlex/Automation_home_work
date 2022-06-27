import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

#  в этом файле мы записываем часто вызываемые фикстуры, для того что б не прописывать их в каждом файле с тестами
