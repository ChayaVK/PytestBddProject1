import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage


class LoginPage:

        username_input = (By.ID,"username")
        password_input = (By.ID,"password")
        login_button = (By.CLASS_NAME,"radius")

        def __init__(self, get_driver):
            self.driver = get_driver

        def enter_username(self,username):
            self.driver.find_element(*self.username_input).send_keys(username)

        def enter_password(self,password):
            self.driver.find_element(*self.password_input).send_keys(password)

        def click_login_button(self):
            self.driver.find_element(*self.login_button).click()

        def login(self):
            self.enter_username("tomsmith")
            self.enter_password("SuperSecretPassword!")
            self.click_login_button()
            return HomePage(self.driver)









