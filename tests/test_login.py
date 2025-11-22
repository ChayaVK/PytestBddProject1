import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage


def test_user_login(get_driver):
    login_page = LoginPage(get_driver)
    h = login_page.login()
    h.verify_message()

