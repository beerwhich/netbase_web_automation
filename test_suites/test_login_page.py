from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import config_manager as conf
from common_util.web.page import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from common_util.logger_manager import LoggerManager


class TestLoginPage(object):

    @classmethod
    def setup_class(cls):
        print("setup_class()")
        cls.options = Options()
        cls.options.add_argument("--headless")
        cls.options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})

    @classmethod
    def teardown_class(cls):
        print("teardown_class()")

    def setup_method(self, method):
        print("setup_method()")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.driver.maximize_window()
        self.page = Page(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.driver.get(conf.INSTAGRAM_LOGIN_PAGE)
        self.page.wait_page()

    def teardown_method(self, method):
        print("teardown_method()")
        self.page.screenshot(method.__name__)
        self.driver.quit()

    def test_instagram_login_with_username(self):
        self.login_page.login_with_account_and_password(account=conf.ACCOUNT_USERNAME, password=conf.ACCOUNT_PASSWORD)
        assert self.home_page.check_if_sign_in() is True, 'Failure: fail to sign in.'

    def test_instagram_login_with_correct_password_but_wrong_username(self):
        self.login_page.login_with_account_and_password(account='netbase123wrong', password=conf.ACCOUNT_PASSWORD)
        assert self.login_page.get_error_message_from_error_message_paragraph() == "The username you entered doesn't belong to an account. Please check your username and try again."

    def test_instagram_login_with_correct_username_but_wrong_password(self):
        self.login_page.login_with_account_and_password(account=conf.ACCOUNT_USERNAME, password='netbase123wrong')
        assert self.login_page.get_error_message_from_error_message_paragraph() == "Sorry, your password was incorrect. Please double-check your password."

    def test_instagram_login_with_wrong_username_and_password(self):
        self.login_page.login_with_account_and_password(account='netbase123wrong', password='netbase123wrong')
        assert self.login_page.get_error_message_from_error_message_paragraph() == "The username you entered doesn't belong to an account. Please check your username and try again."

    def test_instagram_login_with_email(self):
        self.login_page.login_with_account_and_password(account=conf.ACCOUNT_EMAIL, password=conf.ACCOUNT_PASSWORD)
        assert self.home_page.check_if_sign_in() is True, 'Failure: fail to sign in.'
