from selenium.webdriver.common.by import By


class PassportLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    DATE = (By.ID, "birthDate")
    ABOUT = (By.ID, "about")
    PHOTO = (By.ID, "photo")
    SAVE_BUTTON = (By.XPATH, "//button[@data-test='submit-button']")