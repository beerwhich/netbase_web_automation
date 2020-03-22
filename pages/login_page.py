import time

from common_util.web.base import Page
from locators.login_locator import LoginPageLocator


class LoginPage(Page):

    def login_with_account_and_password(self, account, password):
        self.send_text_to_element(LoginPageLocator.ACCOUNT_INPUT_FIELD, account)
        time.sleep(1)
        self.send_text_to_element(LoginPageLocator.PASSWORD_INPUT_FIELD, password)
        time.sleep(1)
        self.click_element(LoginPageLocator.LOGIN_BUTTON)
        time.sleep(1)

    def get_error_message_from_error_message_paragraph(self):
        error_message = self.get_text_from_element(LoginPageLocator.ERROR_MESSAGE_PARAGRAPH)
        return error_message
