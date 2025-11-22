import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def get_driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()