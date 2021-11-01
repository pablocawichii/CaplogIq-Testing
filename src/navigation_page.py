from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, ElementNotInteractableException

import src.home_page as home_page
import src.new_deal_page as new_deal_page

# Create the to return on navigate
def create_home(driver):
    return home_page.HomePage(driver)
def create_favorite(driver):
    return "favorite"
def create_draft(driver):
    return "draft"
def create_folder(driver):
    return "folder"
def create_new_deal(driver):
    return new_deal_page.NewDealPage(driver)


class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

        self.hamburger = (By.XPATH, "//div[@class='app-header--pane']/button[contains(@class,'hamburger')]")
        self.travel = {
            "home": (By.XPATH,
                     "//div[@class='sidebar-navigation']//a[text()='Home']"),
            "favorite":
            (By.XPATH,
             "//div[@class='sidebar-navigation']//a[text()='Favorites']"),
            "draft":
            (By.XPATH,
             "//div[@class='sidebar-navigation']//a[text()='Drafts']"),
            "folder":
            (By.XPATH,
             "//div[@class='sidebar-navigation']//a[text()='Folders']"),
            "new_deal":
            (By.XPATH,
             "//div[@class='app-header-menu']/button[contains(@class,'MuiButton-root')]")
        }

        self.travelReturn = {
            "home": create_home,
            "favorite": create_favorite,
            "draft": create_draft,
            "folder": create_folder,
            "new_deal": create_new_deal
        }

    def goTo(self, place):
        try:
            hamburger_but = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(self.hamburger)
            )
            hamburger_but.click()
        except ElementNotInteractableException:
            pass

        link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located(self.travel[place])
        )
        link.click()

        return self.travelReturn[place](self.driver)
