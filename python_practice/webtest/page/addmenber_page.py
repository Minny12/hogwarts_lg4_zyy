from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AddMenberPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def addmenber(self):
        # 添加姓名
        self.driver.find_element(By.ID, "username").send_keys("aaa1")
        # 添加账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("176587920")
        # 添加手机
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("18724268599")
        # 点击保存
        self.driver.find_element(By.LINK_TEXT, "保存并继续添加").click()
        return AddMenberPage(self.driver)

    def to_contacts(self):
        # 点击返回通讯录页
        locator = (By.ID, "menu_contacts")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        sleep(3)
        self.driver.find_element(By.ID, "menu_contacts").click()
        from python_practice.webtest.page.menucontacts_page import MenuContactsPage
        return MenuContactsPage(self.driver)