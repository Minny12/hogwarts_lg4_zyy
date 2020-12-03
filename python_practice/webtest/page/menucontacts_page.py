from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from python_practice.webtest.page.addmenber_page import AddMenberPage


class MenuContactsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def to_add_member(self):
        locator = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_elements(By.CSS_SELECTOR, ".ww_operationBar .js_add_member")[0]
        element.click()
        return AddMenberPage(self.driver)
