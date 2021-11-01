from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.common.exceptions import TimeoutException

import src.navigation_page as navigation_page

import time

def select_drop_down(driver, select, option_dropdown, option_value, ind=-1):
    if(ind < 0):
        select_id = (By.ID, select)
        select_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(select_id) and ec.element_to_be_clickable(select_id)
        )
        select_input.click()
    else:
        select_id = (By.XPATH, f"//form/div[{ind}]//div[@id='{select}']")
        select_input = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(select_id)
            and ec.element_to_be_clickable(select_id))
        select_input.click()

    select_option_id = (By.XPATH, f"//div[@id='{option_dropdown}']//ul/li[text()='{option_value}']")
    select_option_input = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(select_option_id)
    )
    select_option_input.click()

def input_on_name(driver, name, keys, ind=1):
    input_name = (By.XPATH, f"//form/div[{ind}]//input[@name='{name}']")
    input = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located(input_name) and ec.element_to_be_clickable(input_name)
    )
    input.send_keys(keys)

# This is the home dashboard
class NewDealPage:
    def __init__(self, driver):
        self.driver = driver

    # Check if deal processed
    def check(self):
        return "X"

    def new_deal_one(self, data):
        name = (By.NAME, "dealName")
        finance = (By.NAME, "financingRequest")
        team = (By.XPATH, f"//div[contains(@class,'MuiPaper-root')]/ul/li[text()= '{data['team']}']")
        team_sel = (By.ID, "mui-component-select-team")
        program = (By.XPATH, f"//div[contains(@class,'MuiPaper-root')]/ul/li[text()= '{data['program']}']")
        program_sel = (By.ID, "mui-component-select-loanProgram")

        try:
            name_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(name)
            )
            name_inp.clear()
            name_inp.send_keys(data['name'])

            finance_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(finance)
            )
            finance_inp.clear()
            finance_inp.send_keys(data['finance'])

            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(team_sel)
            ).click()

            team_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(team)
            )
            team_inp.click()

            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(program_sel) and ec.element_to_be_clickable(program_sel)
            ).click()

            program_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(program)
            )
            program_inp.click()

            sponsor_type = (By.XPATH, f"//input[@value='{data['sponsor_type']}']")
            sponsor_sel = (By.ID, "mui-component-select-sponsor")
            sponsor = (By.XPATH, f"//div[contains(@class,'MuiPaper-root')]/ul/li[text()= '{data['sponsor']}']")

            sponsor_type_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(sponsor_type)
            )
            sponsor_type_inp.click()

            sponsor_sel_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(sponsor_sel)
            )
            sponsor_sel_inp.click()

            sponsor_inp = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(sponsor)
            )
            sponsor_inp.click()

            time.sleep(5)

            next_button = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((
                    By.XPATH,
                    "//button[contains(@class, 'MuiButtonBase-root MuiButton-root')][@type='submit']"
                )))

            next_button.click()

        except TimeoutException:
            return False

        try:
            err = (By.XPATH, "//p[@class='MuiFormHelperText-root Mui-error']")
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(err)
            )
            return False
        except TimeoutException:
            return True

    def new_deal_two(self, data):
        # Preperation
        close_all_xpath = (By.XPATH, "//div[@class='MuiTabs-flexContainer']/button[contains(@class,'MuiButtonBase-root')]/span/*[@class='MuiSvgIcon-root']")

        try:

            close_all = WebDriverWait(self.driver, 3).until(
                ec.presence_of_all_elements_located(close_all_xpath)
            )

            close_all.reverse()

            for close in close_all:
                close.click()
                time.sleep(1)
        except TimeoutException:
            print("No Properties")

        time.sleep(4)

        new_xpath = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.XPATH, "//div[contains(@class,'MuiGrid-root')]/button[contains(@class,'MuiButtonBase-root')]/span/*[@class='MuiSvgIcon-root']/../.."))
            )

        # Filling in info for each property
        for ind, property in enumerate(data['properties']):
            new_xpath.click()

            time.sleep(5)

            current_property = (By.XPATH, f"//div[@class='MuiTabs-flexContainer']/button[contains(@class,'MuiButtonBase-root')][{ind+1}]")
            current_property_button = self.driver.find_element(current_property[0], current_property[1])
            current_property_button.click()

            time.sleep(3)

            input_on_name(self.driver, f"properties[{ind}].propertyName", property.get('name','0'), ind+1)

            select_drop_down(self.driver, f"mui-component-select-properties[{ind}].propertyType", f"menu-properties[{ind}].propertyType", property.get("type",'0'))
            select_drop_down(self.driver, f"mui-component-select-properties[{ind}].propertySubType", f"menu-properties[{ind}].propertySubType", property.get("subtype",'0'))
            select_drop_down(self.driver, f"mui-component-select-properties[{ind}].financingPurpose", f"menu-properties[{ind}].financingPurpose", property.get("purpose",'0'))
            select_drop_down(self.driver, f"mui-component-select-properties[{ind}].secondaryPropertyType", f"menu-properties[{ind}].secondaryPropertyType", property.get("secondaryPropertyType","Other"))
            input_on_name(self.driver, f"properties[{ind}].secondaryPropertyTypeNumberOfUnits", property.get("secondaryPropertyTypeNumberOfUnits",'0'), ind+1)

            input_on_name(self.driver, "numberOfUnits", property.get("numberOfUnits",'0'), ind+1)
            input_on_name(self.driver, "siteArea", property.get("siteArea",'0'), ind+1)
            input_on_name(self.driver, "yearBuilt", property.get("yearBuilt",'0'), ind+1)
            input_on_name(self.driver, "yearRenovated", property.get("yearRenovated",'0'), ind+1)
            input_on_name(self.driver, "acquisitionCost", property.get("acquisitionCost",'0'), ind+1)
            input_on_name(self.driver, "improvementPlan", property.get("improvementPlan",'0'), ind+1)
            input_on_name(self.driver, "fees", property.get("fees",'0'), ind+1)

            select_drop_down(self.driver, "group", "menu-docType", property.get("group",'Rent Roll'), ind+1)

            # I need to learn how to add files dynamically using dropboxes like this one
            # I can do it only with basic file inputs
            browse_xpath = (By.XPATH, f"//form/div[{ind+1}]//span[@class='px-2']")
            browse_files = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(browse_xpath) and ec.element_to_be_clickable(browse_xpath)
            )
            browse_files.click()

            time.sleep(30)

        next_button = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((
                    By.XPATH,
                    "//button[contains(@class, 'MuiButtonBase-root MuiButton-root')][@type='submit']"
                )))

        next_button.click()

        # Checking for error
        try:
            err = (By.XPATH, "//p[@class='MuiFormHelperText-root Mui-error']")
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located(err)
            )

            return False
        except TimeoutException:
            return True

    def new_deal_three(self):
        time.sleep(30)

        next_button = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((
                By.XPATH,
                "//button[contains(@class, 'MuiButtonBase-root MuiButton-root')][@type='submit']"
            )))

        next_button.click()

        # Checking for error
        try:
            err = (By.XPATH, "//p[@class='MuiFormHelperText-root Mui-error']")
            WebDriverWait(self.driver,10).until(ec.presence_of_element_located(err))
            return False
        except TimeoutException:
            return True


    # Navigate using navigation page
    def navigateTo(self, place):

        nav = navigation_page.NavigationPage(self.driver)
        return nav.goTo(place)
