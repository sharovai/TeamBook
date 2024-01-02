from page_objects.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver


# noinspection PyProtectedMember,PyUnresolvedReferences
class LoginPage(BasePage):
    __url = "https://web.teambooktest.com/login"
    __user_name = (By.XPATH, "//input[@id=':r0:']")
    __password = (By.XPATH, "//input[@id=':r1:']")
    __login_button = (By.XPATH, "//button[@id='login_btn']")
    __error_message = (By.XPATH, "//p[@class='form-error__main-text']")

    def __init__(self, driver: WebDriver):
        super().__int__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username, password, ):
        super()._type(self.__user_name, username)
        super()._type(self.__password, password)
        super()._click(self.__login_button)

    def error_message(self) -> str:
        return super()._get_text(self.__error_message)
