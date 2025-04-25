import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://berpress.github.io/ui-passport-demo/"

@pytest.mark.skip
class TestQa:
    def test_add_all_data(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        # elements
        name = driver.find_element(By.ID, "firstName")
        last_name = driver.find_element(By.ID, "lastName")
        calendar = driver.find_element(By.ID, "birthDate")
        about = driver.find_element(By.ID, "about")
        photo = driver.find_element(By.ID, "photo")
        file_path = os.path.abspath("1.png")
        save_button = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # do
        name.send_keys('Иван')
        last_name.send_keys('Иванов')
        calendar.send_keys("08.12.1980")
        about.send_keys('Test QA')
        photo.send_keys(file_path)
        save_button.click()
        # time.sleep(5)
        driver.quit()

    def test_add_data_minimal_name(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        # elements
        name = driver.find_element(By.ID, "firstName")
        last_name = driver.find_element(By.ID, "lastName")
        calendar = driver.find_element(By.ID, "birthDate")
        about = driver.find_element(By.ID, "about")
        photo = driver.find_element(By.ID, "photo")
        file_path = os.path.abspath("1.png")
        save_button = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # do
        name.send_keys('Ив')
        last_name.send_keys('Иванов')
        calendar.send_keys("08.12.1980")
        about.send_keys('Test QA')
        photo.send_keys(file_path)
        save_button.click()
        # time.sleep(5)
        driver.quit()

    def test_add_data_invalid_name(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        # elements
        name = driver.find_element(By.ID, "firstName")
        last_name = driver.find_element(By.ID, "lastName")
        calendar = driver.find_element(By.ID, "birthDate")
        about = driver.find_element(By.ID, "about")
        photo = driver.find_element(By.ID, "photo")
        file_path = os.path.abspath("1.png")
        save_button = driver.find_element(By.XPATH, "//button[@data-test='submit-button']")
        # do
        name.send_keys('И')
        last_name.send_keys('Иванов')
        calendar.send_keys("08.12.1980")
        about.send_keys('Test QA')
        photo.send_keys(file_path)
        save_button.click()
        # time.sleep(5)
        driver.quit()