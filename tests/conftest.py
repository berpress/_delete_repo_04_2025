import random

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.passport import Passport
from pages.passport_1 import Passport2
from pages.passport_2 import Passport3


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://berpress.github.io/ui-passport-demo/",
                     help="url")


@pytest.fixture(scope="session")
def passport_page(request):
    url = request.config.getoption("--url")
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")  # Установка размера окна
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    yield Passport3(driver)
    driver.quit()

@pytest.fixture(scope="function")
def number(request):
    return 1

@pytest.fixture(scope="function")
def get_random_number():
    number = random.randint(1, 100)
    return number