from typing import Type
import pytest
from selenium import webdriver
import src.login_page as login_page
import src.home_page as home_page

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.get("https://www.cap2.caplogiq.com/")

    return driver

def test_login(driver):
    login = login_page.LoginPage(driver)

    data = {
        "email": "pablocawichii@gmail.com",
        "password": "password123"
    }

    home = login.login(data)
    assert type(home) is home_page.HomePage
    driver.quit()
