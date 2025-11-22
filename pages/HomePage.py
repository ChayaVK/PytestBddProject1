import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, get_driver):
        self.driver = get_driver

    success_message = (By.XPATH,"//div[@id='flash-messages']/div")

    def verify_message(self):
        m = self.driver.find_element(*self.success_message).text
        message = m.replace("\n","").replace("×","")
        print(message)
        assert message == "You logged into a secure area!"