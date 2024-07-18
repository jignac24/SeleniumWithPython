import pytest
from selenium import webdriver

from config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    elif request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.get(TestData.BaseURL)
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
