from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import TimeoutException

import src.navigation_page as navigation_page
import src.new_deal_page as new_deal_page

# This is the home dashboard
class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # Check if deal processed
    def check_for_draft(self, data):
        title = (By.XPATH, f"//div[@class='property-date'][contains(text(), '{data['team']}')]/..//b[text()='{data['name']}']")

        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(title)
            )

            return True
        except TimeoutException:
            return False

    def edit_draft(self, data):
        if self.check_for_draft(data) is not True:
            return False

        button = (By.XPATH, f"//div[@class='property-date'][contains(text(), '{data['team']}')]/..//b[text()='{data['name']}']/../..//button")


        button_inp = WebDriverWait(self.driver,
                        10).until(ec.presence_of_element_located(button))

        button_inp.click()

        return new_deal_page.NewDealPage(self.driver)



    # Navigate using navigation page
    def navigateTo(self, place):

        nav = navigation_page.NavigationPage(self.driver)
        return nav.goTo(place)
