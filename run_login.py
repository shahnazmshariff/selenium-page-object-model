import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from LoginPage import LoginPage
from locators import LoginPageLocators

class RunLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/home/shahnaz/Downloads/chromedriver')

    def test_login(self):
        ## get url
        login_page = LoginPage(self.driver)

        login_page.open_login_page()

        login_page.add_username()

        login_page.add_password()

        login_page.click_submit_button()

    def tearDown(self):
        self.driver.quit()








