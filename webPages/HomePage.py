import time

from selenium.webdriver.common.by import By

from webPages.BasePage import BasePage


class HomePage(BasePage):
    radioButtons = (By.CSS_SELECTOR, 'div[id="radio-btn-example"] fieldset label')

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_title()

    def get_radio_button(self):
        elements = self.get_radioButton(self.radioButtons)
        for element in elements:
            # print(element.find_element(By.CSS_SELECTOR, "input[class='radioButton']").get_attribute('value'))
            element.find_element(By.CSS_SELECTOR, "input[class='radioButton']").click()
            time.sleep(2)
