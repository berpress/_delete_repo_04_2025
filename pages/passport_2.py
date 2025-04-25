import logging

from locators.passport_locators import PassportLocators
from pages.base_page import BasePage

logger = logging.getLogger("qa")



class Passport3(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_passport(self, name_text: str, last_name_text: str, calendar_text: str, about_text: str):
        logger.info(f'Try to add passport: name {name_text},'
                    f' last name {last_name_text},'
                    f' date {calendar_text}')
        self.fill(value=name_text, locator=PassportLocators.FIRST_NAME)
        self.fill(value=last_name_text, locator=PassportLocators.LAST_NAME)
        self.fill(value=calendar_text, locator=PassportLocators.DATE)
        self.fill(value=about_text, locator=PassportLocators.ABOUT)
        self.click(locator=PassportLocators.SAVE_BUTTON)

    def get_table(self):
        return self.text(locator=PassportLocators.USER_TABLE)