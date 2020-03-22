from selenium.common.exceptions import NoSuchElementException
from common_util.web.base import Page
from locators.home_page_locator import HomePageLocator


class HomePage(Page):

    def check_if_sign_in(self):
        try:

            text_suggestion_title = self.get_text_from_element(HomePageLocator.SUGGESTION_TITLE)
            if text_suggestion_title == 'Suggestions For You':
                return True
            else:
                return False
        except NoSuchElementException:
            return False
