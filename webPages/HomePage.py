from webPages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_page_title(self):
        return self.get_title()
