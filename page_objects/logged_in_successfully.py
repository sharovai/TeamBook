from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://web.teambooktest.com/planners/5298/2023-12-18"
    __user_profile = (By.XPATH, "//div[@id='openUserMenu']")

    def __init__(self, driver: WebDriver):
        super().__int__(driver)

    def current_url(self) -> str:
        return self._driver.current_url

    def user_profile_is_displayed(self):
        return super()._is_displayed(self.__user_profile)
