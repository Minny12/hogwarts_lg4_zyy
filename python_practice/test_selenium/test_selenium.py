import selenium
import pytest
from selenium import webdriver


def test_1():
    print("1")


def test_baidu():
    print("执行完毕！")
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    print("1")


def test_hello():
    print("1")
    print("执行完毕！")
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    print("1")
