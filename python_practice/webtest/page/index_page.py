from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from python_practice.webtest.page.menucontacts_page import MenuContactsPage


class IndexPage:
    def __init__(self):
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.implicitly_wait(5)

    def to_menu_contacts(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        return MenuContactsPage(self.driver)
