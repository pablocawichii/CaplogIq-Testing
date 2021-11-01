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


def test_create_new_deal(driver):
    login = login_page.LoginPage(driver)

    data = {"email": "pablocawichii@gmail.com", "password": "password123"}

    home = login.login(data)

    new_deal = home.navigateTo("new_deal")

    data = {
        'name': "New Deal",
        'finance': '4100',
        'team': 'Demo Team',
        'program': 'CMBS Loan Program',
        'sponsor_type': 'business',
        'sponsor': 'Demo Sponsor'
    }

    assert new_deal.new_deal_one(data) is True

    data = {
        'properties': [{
            "name": 'PcServices',
            "type": 'Office',
            "subtype": 'Suburban',
            "purpose": 'Refinance',
            "numberOfUnits": '1234',
            "siteArea": '4321',
            "yearBuilt": '2000',
            "yearRenovated": '2015',
            "acquisitionCost": '50000',
            "group": 'Rent Roll'
        }]
    }

    assert new_deal.new_deal_two(data) is True

    assert new_deal.new_deal_three() is True
    driver.quit()


def test_create_new_deal_draft(driver):
    login = login_page.LoginPage(driver)

    data = {"email": "pablocawichii@gmail.com", "password": "password123"}

    home = login.login(data)

    new_deal = home.navigateTo("new_deal")

    data = {
        'name': "New Deal Through Draft",
        'finance': '1200',
        'team': 'Demo Team',
        'program': 'CMBS Loan Program',
        'sponsor_type': 'business',
        'sponsor': 'Demo Sponsor'
    }

    assert new_deal.new_deal_one(data) is True

    home = new_deal.navigateTo("home")
    new_deal = home.edit_draft(data)
    assert new_deal.new_deal_one(data) is True

    data = {
        'properties': [{
            "name": 'PcServices',
            "type": 'Office',
            "subtype": 'Suburban',
            "purpose": 'Refinance',
            "numberOfUnits": '1234',
            "siteArea": '4321',
            "yearBuilt": '2000',
            "yearRenovated": '2015',
            "acquisitionCost": '50000',
            "group": 'Rent Roll'
        }]
    }

    assert new_deal.new_deal_two(data) is True

    assert new_deal.new_deal_three() is True
    driver.quit()
