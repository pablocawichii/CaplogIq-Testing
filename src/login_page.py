from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import TimeoutException

import src.home_page as home_page

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.email = "username"
        self.password = "password"
        self.sign_in = "//div[@class='text-center py-4']/button[contains(@class,'MuiButton-root')]"
        self.error = "//div[@class='MuiDialog-root']"

    def login(self, data):

        email_inp = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, self.email))
        )

        password_inp = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.NAME, self.password)))

        sign_in_inp = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, self.sign_in)))



        email_inp.send_keys(data["email"])
        password_inp.send_keys(data["password"])
        sign_in_inp.click()

        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, self.error)))
            return "An Error Has Occurred"
        except TimeoutException:
            return home_page.HomePage(self.driver)
