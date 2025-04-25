import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.passport import Passport

URL = "https://berpress.github.io/ui-passport-demo/"

@pytest.mark.skip
class TestQa2:
    def test_add_all_data_2(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        passport_page = Passport(driver)
        file_path = os.path.abspath("1.png")
        passport_page.add_passport(name_text="Иван", last_name_text="Иванов", calendar_text="08.12.1980", about_text="About", photo_path=file_path)
        time.sleep(10)
        driver.quit()

    def test_add_data_minimal_name_2(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        passport_page = Passport(driver)
        file_path = os.path.abspath("1.png")
        passport_page.add_passport(name_text="Ив", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About", photo_path=file_path)
        time.sleep(10)
        driver.quit()

    def test_add_data_invalid_name_2(self):
        driver = webdriver.Chrome()
        driver.get(URL)
        passport_page = Passport(driver)
        file_path = os.path.abspath("1.png")
        passport_page.add_passport(name_text="И", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About", photo_path=file_path)
        time.sleep(10)
        driver.quit()