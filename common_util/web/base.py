import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from common_util.logger_manager import LoggerManager
from config import config_manager


class Page(object):
    def __init__(self, driver):
        self.log = LoggerManager.get_instance()
        self.driver = driver if driver != '' else webdriver.Chrome(ChromeDriverManager().install())

        self.driver.implicitly_wait(config_manager.DEFAULT_TIMEOUT)

        if not os.path.exists(config_manager.SCREENSHOTS_DIR_PATH):
            os.makedirs(config_manager.SCREENSHOTS_DIR_PATH)

        if not os.path.exists(os.path.join(config_manager.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d"))):
            os.makedirs(os.path.join(config_manager.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d")))

    # ======================= single element ====================== #
    def find_element(self, locator):
        # TODO check if screenshot needed
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def is_find_element(self, locator):
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_attr_from_element(self, locator, attr):
        element = self.find_element(locator)
        return element.get_attribute(attr)

    def get_text_from_element(self, locator):
        element = self.find_element(locator)
        return element.text

    def send_text_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def wait_page(self):
        self.driver.implicitly_wait(config_manager.DEFAULT_TIMEOUT)

    # ======================= multiple elements ====================== #
    def __get_elements_by_locator(self, locator, timeout_msg):
        elements = WebDriverWait(self.driver).until(EC.visibility_of_all_elements_located(locator), timeout_msg)
        return elements

    def find_elements(self, locator, timeout_msg=''):
        elements = self.__get_elements_by_locator(locator, timeout_msg)
        return elements

    def click_list_item(self, locator, pos, timeout=config_manager.DEFAULT_TIMEOUT, poll_frq=1):
        element = self.find_elements(locator, timeout, poll_frq)[pos]
        element.click()

    def click_list_item_by_text(self, locator, text, timeout=config_manager.DEFAULT_TIMEOUT, poll_frq=1):
        for element in self.find_elements(locator, timeout, poll_frq):
            if text == element.text:
                element.click()

    def get_texts_from_elements(self, locator, timeout=config_manager.DEFAULT_TIMEOUT, poll_frq=1):
        elements = self.find_elements(locator, timeout, poll_frq)
        texts_at_elements = list()
        for element in elements:
            texts_at_elements.append(element.text)
        return texts_at_elements

    def scroll_page(self, locator):
        ActionChains(self.driver).move_to_element(self.find_element(locator)).perform()

    # ======================= screenshots ====================== #
    def screenshots(self, method_name):
        try:
            screenshots_name = '{now}_{name}.png'.format(now=time.strftime("%Y%m%d%H%M%S"), name=method_name)
            screenshots_path = os.path.join(config_manager.SCREENSHOTS_DIR_PATH, time.strftime("%Y%m%d"),
                                            screenshots_name)

            self.log.info("Taking screenshots: {abs_path}".format(abs_path=screenshots_path))
            self.driver.get_screenshot_as_file(screenshots_path)

        except Exception as e:
            self.log.error(e)
