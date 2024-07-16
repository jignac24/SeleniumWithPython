import pytest

from config.config import TestData
from webPages.HomePage import HomePage
from webTests.test_basePage import BaseTest


class Test_HomePage(BaseTest):

    def test_title(self):
        self.homepage = HomePage(self.driver)
        assert self.homepage.get_page_title() == TestData.PageTitle



