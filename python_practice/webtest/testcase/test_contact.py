from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from python_practice.webtest.page.index_page import IndexPage


class TestWX:

    def setup(self):
        self.indexpage = IndexPage()

    def test_case1(self):
        self.indexpage.to_menu_contacts().to_add_member().addmenber().to_contacts()
