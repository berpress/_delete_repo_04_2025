from locators.passport_locators import PassportLocators
from pages.base_page import BasePage


class Passport3(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_passport(self, name_text: str, last_name_text: str, calendar_text: str, about_text: str, photo_path=None):
        self.fill(value=name_text, locator=PassportLocators.FIRST_NAME)
        self.fill(value=last_name_text, locator=PassportLocators.LAST_NAME)
        self.fill(value=calendar_text, locator=PassportLocators.DATE)
        self.fill(value=about_text, locator=PassportLocators.ABOUT)
        self.click(locator=PassportLocators.SAVE_BUTTON)