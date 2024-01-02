import time
from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestAuthorization:

    def test_auth_positive(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("testhardandstudy@yahoo.com", 'B16177120b')
        logged_in_page = LoggedInSuccessfullyPage(driver)
        time.sleep(3)
        assert logged_in_page.user_profile_is_displayed()

    def test_auth_negative_username(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("testhardandstudy@yahoo", 'B16177120b')
        time.sleep(3)
        assert login_page.error_message() == "There was an error:"


    def test_auth_negative_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login("testhardandstudy@yahoo.com", 'B161771')
        time.sleep(3)
        assert login_page.error_message() == "There was an error:"

