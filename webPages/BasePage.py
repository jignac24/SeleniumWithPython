from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This is base page of all the web pages in the framework"""


class BasePage:

    # constructor of Base class
    def __init__(self, driver):
        self.driver = driver

    def clicks(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def get_title(self):
        # WebDriverWait(self.driver,10).until(EC.title_is(self.driver.title))
        return self.driver.title

    def sendkeys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def element_enabled(self, by_locator) -> bool:
        element = WebDriverWait(self.driver,10).until(EC.p(by_locator))
        return element.is_enabled()

    def select_dropdown(self, by_locator, value):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        select = Select(element)
        select.select_by_value(value)

    def get_radioButton(self, by_locator):
        element = WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(by_locator))
        return element
