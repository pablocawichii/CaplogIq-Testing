from selenium import webdriver

import src.login_page as login_page
import time

driver = webdriver.Firefox()

driver.get("https://www.cap2.caplogiq.com/")
driver.maximize_window()

login = login_page.LoginPage(driver)

data = {
    "email": "pablocawichii@gmail.com",
    "password": "password123"
}

# Failure
# print(login.login(data))

# Success
home = login.login(data)


data = {
    'name': "Testing",
    'finance': '4500',
    'team': 'Demo Team',
    'program': 'CMBS Loan Program',
    'sponsor_type': 'business',
    'sponsor': 'Demo Sponsor'
}

new_deal = home.edit_draft(data)
X = new_deal.new_deal_one(data)
print(X)
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
    }, {
        "name": 'PcServices 2',
        "type": 'Office',
        "subtype": 'Suburban',
        "purpose": 'Refinance',
        "numberOfUnits": '4321',
        "siteArea": '1234',
        "yearBuilt": '2000',
        "yearRenovated": '2015',
        "acquisitionCost": '50000',
        "group": 'Rent Roll'
    }]
}

Y = new_deal.new_deal_two(data)
print(Y)


driver.quit()
