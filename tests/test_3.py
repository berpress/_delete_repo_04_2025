import os
import time

import pytest


@pytest.mark.skip
class TestQa3:

    def test_add_all_data_3(self, passport_page):
        file_path = os.path.abspath("1.png")
        passport_page.add_passport(name_text="Иван", last_name_text="Иванов", calendar_text="08.12.1980", about_text="About", photo_path=file_path)
        # time.sleep(10)


    def test_add_data_minimal_name_3(self, passport_page):
        file_path = os.path.abspath("1.png")
        passport_page.add_passport(name_text="Ив", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About", photo_path=file_path)
        # time.sleep(10)

    def test_add_data_invalid_name_3(self, passport_page):
        file_path = os.path.abspath("1.png")
        passport_page.add_passport(name_text="И", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About", photo_path=file_path)
        # time.sleep(10)