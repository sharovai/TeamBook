from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __int__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator, text):
        return self._find(locator).send_keys(text)

    def _click(self, locator: tuple):
        self._find(locator).click()

    def _user_profile(self, locator):
        return self._find(locator)

    def _is_displayed(self, locator: tuple) -> bool:
        return self._find(locator).is_displayed()

    def _get_text(self, locator):
        return self._find(locator).text
