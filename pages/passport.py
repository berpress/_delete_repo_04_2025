from selenium.webdriver.common.by import By


class Passport:
    def __init__(self, driver):
        self.driver = driver
        self.name = driver.find_element(By.ID, "firstName")
        self.last_name = driver.find_element(By.ID, "lastName")
        self.calendar = driver.find_element(By.ID, "birthDate")
        self.about = driver.find_element(By.ID, "about")
        self.photo = driver.find_element(By.ID, "photo")
        self.save_button = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")

    def add_passport(self, name_text: str, last_name_text: str, calendar_text: str, about_text: str, photo_path):
        name = self.driver.find_element(By.ID, "firstName")
        last_name = self.driver.find_element(By.ID, "lastName")
        calendar = self.driver.find_element(By.ID, "birthDate")
        about = self.driver.find_element(By.ID, "about")
        photo = self.driver.find_element(By.ID, "photo")
        save_button = self.driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # do
        name.send_keys(name_text)
        last_name.send_keys(last_name_text)
        calendar.send_keys(calendar_text)
        about.send_keys(about_text)
        photo.send_keys(photo_path)
        save_button.click()