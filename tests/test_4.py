import os


class TestQa4:

    def test_add_all_data_4(self, passport_page):
        passport_page.add_passport(name_text="Иван", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About")
        # time.sleep(10)


    def test_add_data_minimal_name_4(self, passport_page):
        passport_page.add_passport(name_text="Ив", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About")
        # time.sleep(10)

    def test_add_data_invalid_name_4(self, passport_page):
        passport_page.add_passport(name_text="И", last_name_text="Иванов", calendar_text="08.12.1980",
                                   about_text="About")
        # time.sleep(10)