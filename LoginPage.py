from selenium import webdriver
from BasePage import Page
from locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(Page):
    def open_login_page(self):
        self.open(url='http://130.15.4.122/cubemail/')

    def add_username(self):
        element = self.find_element(*LoginPageLocators.Username)
        element.send_keys('shahnaz')

    def add_password(self):
        element = self.find_element(*LoginPageLocators.Password)
        element.send_keys('########')

    def click_submit_button(self):
        """Triggers the submit"""
        element = self.find_element(*LoginPageLocators.Submit)
        element.click()


