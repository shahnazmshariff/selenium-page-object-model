from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    """A class for login page locators. All login page locators should come here"""
    Username = (By.ID, 'rcmloginuser')
    Password = (By.ID, 'rcmloginpwd')
    Submit = (By.ID, 'rcmloginsubmit')