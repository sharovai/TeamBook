import pytest
from selenium import webdriver

from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver():
    my_driver = webdriver.Chrome()
    yield my_driver


