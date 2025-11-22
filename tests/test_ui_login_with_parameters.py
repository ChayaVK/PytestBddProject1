import pytest
from selenium import webdriver
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By


scenarios("../features/ui_login_with_parameters.feature")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@given ("user lands on to login page")
def open_login_page(driver):
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

@when(parsers.parse("user enter {username} and {password}"))
def enter_username_password(driver,username,password):
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CLASS_NAME, "radius").click()

@then(parsers.parse("user should be able to see right {uimessage}"))
def verify_logout_button(driver,uimessage):
        entiremessage =  driver.find_element(By.XPATH, "//div[@id='flash-messages']/div").text
        message = entiremessage.replace("\n","").replace("×","")
        assert message == uimessage






