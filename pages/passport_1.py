import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Passport2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.name = (By.ID, "firstName")
        self.last_name = (By.ID, "lastName")
        self.calendar = (By.ID, "birthDate")
        self.about = (By.ID, "about")
        self.photo = (By.ID, "photo")
        self.save_button = (By.XPATH, "//button[@data-test='submit-button']")

    def add_passport(self, name_text: str, last_name_text: str, calendar_text: str, about_text: str, photo_path):
        self.fill(value=name_text, locator=self.name)
        self.fill(value=last_name_text, locator=self.last_name)
        self.fill(value=calendar_text, locator=self.calendar)
        self.fill(value=about_text, locator=self.about)
        self.fill(value=photo_path, locator=self.photo)
        self.click(locator=self.name)