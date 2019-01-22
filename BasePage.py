from selenium import webdriver
from selenium.webdriver.common.by import By

class Page(object):
    """
    Base class that all page models can inherit from
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def open(self, url):
        self.driver.get(url)
