import allure
import pytest
from pytest_bdd.types import GIVEN
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
import allure_pytest

scenarios("../features/ui_login.feature")

@given ("user lands on to login page")
@allure.step("User on login page")
def open_login_page(driver):
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

@when("user enter username and password")
@allure.step("user enter username and password")
def enter_username_password(driver):
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CLASS_NAME, "radius").click()

@then("user should be able to login successfully")
@allure.step("user should be able to login successfully")
def verify_logout_button(driver):
        emessage =  driver.find_element(By.XPATH, "//div[@id='flash-messages']/div").text
        message = emessage.replace("\n","").replace("×","")
        allure.attach(driver.get_screenshot_as_png(),name="login",attachment_type=allure.attachment_type.PNG)
        assert message == "You logged into a secure area!"






